import "../styles/globals.css";
import { Button } from "@/components/ui/button";
import { ShieldCheck } from "lucide-react";
import { ShieldAlert } from "lucide-react";
import { ShieldQuestion } from "lucide-react";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";

import { ThemeProvider } from "@/components/theme-provider";

import denisLogo from "../img/denis.png";
import browser from "webextension-polyfill";
import { MutableRefObject, useEffect, useRef, useState } from "react";

function timeSince(date: Date) {
  var seconds = Math.floor(((new Date() as any) - (date as any)) / 1000);

  var interval = seconds / 31536000;

  if (interval > 1) {
    return Math.floor(interval) + " years ago";
  }
  interval = seconds / 2592000;
  if (interval > 1) {
    return Math.floor(interval) + " months ago";
  }
  interval = seconds / 86400;
  if (interval > 1) {
    return Math.floor(interval) + " days ago";
  }
  interval = seconds / 3600;
  if (interval > 1) {
    return Math.floor(interval) + " hours ago";
  }
  interval = seconds / 60;
  if (interval > 1) {
    return Math.floor(interval) + " minutes ago";
  }
  return "just now";
}

export default function () {
  const ws: MutableRefObject<WebSocket | null> = useRef(null);
  const [baseUrl, setBaseUrl] = useState("");
  const [baseUrlWithPrefix, setBaseUrlWithPrefix] = useState("");
  const [ts, setTs] = useState<Date | null>(null);
  const [score, setScore] = useState(-1);
  const [fetching, setFetching] = useState<boolean>(false);

  useEffect(() => {
    const getBaseUrl = async () => {
      try {
        // Query the currently active tab in the current window
        const [tab] = await browser.tabs.query({
          active: true,
          currentWindow: true,
        });

        console.log(tab);

        if (tab && tab.url) {
          // Create a URL object to easily extract the base URL
          const url = new URL(tab.url);

          console.log(url);

          // Extract the base URL (protocol + host)
          setBaseUrl(url.host);
          setBaseUrlWithPrefix(url.origin);

          console.log(baseUrlWithPrefix);
        }
      } catch (error) {
        console.error("Failed to get the active tab's URL:", error);
      }
    };

    getBaseUrl();
  }, []);

  useEffect(() => {
    ws.current = new WebSocket("ws://0.0.0.0:6969");

    ws.current.onopen = () => {
      ws.current!.send(
        JSON.stringify({ type: "request_cache", url: baseUrlWithPrefix })
      );
    };

    ws.current.onmessage = (msg: MessageEvent<any>) => {
      const data = JSON.parse(msg.data);

      console.log(data);

      if (data.type === "scan_results") {
        setScore(data.score);
        setFetching(false);
        setTs(new Date());
      } else if (data.type == "cache_found") {
        setScore(data.score);
        setTs(new Date(data.ts));
      }
    };

    return () => {
      if (ws.current) {
        ws.current.close();
      }
    };
  }, [baseUrl, baseUrlWithPrefix]);

  return (
    <ThemeProvider defaultTheme="light">
      <TooltipProvider>
        <div className="flex flex-col gap-3 m-3 h-full ">
          <Card className="p-2">
            <CardTitle>
              <div className="flex items-center justify-between">
                <span className="p-2">DenisDefend</span>
                <div>
                  <img className="h-[2.5rem] w-auto" src={denisLogo} />
                </div>
              </div>
            </CardTitle>
          </Card>
          <Card
            style={{
              backgroundImage:
                score < 0
                  ? undefined
                  : `linear-gradient(to bottom right, ${
                      score < 0.5 ? "rgb(255, 8, 0)" : "rgb(182, 244, 146)"
                    }, rgb(255, 255, 255))`,
            }}
          >
            <CardHeader>
              <CardTitle>
                {!(score < 0) ? (
                  <Tooltip>
                    <TooltipTrigger>
                      <div className="flex gap-2 items-center min-w-0">
                        {baseUrl ? baseUrl : "Loading..."}
                        {(score < 1/2) ? <ShieldAlert /> : <ShieldCheck />}
                      </div>
                    </TooltipTrigger>
                    <TooltipContent>
                      <p>Trust: {`${score*100}%`}</p>
                    </TooltipContent>
                  </Tooltip>
                ) : (baseUrl ? (
                  baseUrl
                ) : (
                  "Loading..."
                )) 
                }
              </CardTitle>
              <CardDescription>
                {ts ? `last scan ${timeSince(ts)}` : "never scanned"}
              </CardDescription>
            </CardHeader>
            <CardContent className="w-full"></CardContent>
            {/* <CardFooter>
          <p>Card Footer</p>
        </CardFooter> */}
          </Card>
          <Button
            disabled={fetching}
            onClick={() => {
              setFetching(true);
              ws.current?.send(
                JSON.stringify({ type: "request_scan", url: baseUrlWithPrefix })
              );
            }}
          >
            {fetching ? (
              <svg
                className="animate-spin h-5 w-5 text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  stroke-width="4"
                ></circle>
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
            ) : score < 0 ? (
              "Scan page"
            ) : (
              "Scan again"
            )}
          </Button>
        </div>
      </TooltipProvider>
    </ThemeProvider>
  );
}
