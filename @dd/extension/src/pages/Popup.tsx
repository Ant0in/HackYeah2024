import "../styles/globals.css";
import { Button } from "@/components/ui/button";
import { CircleCheck } from "lucide-react";
import { Shield } from "lucide-react";
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

export default function () {
  const ws: MutableRefObject<WebSocket | null> = useRef(null);
  const [baseUrl, setBaseUrl] = useState("");

  useEffect(() => {
    ws.current = new WebSocket("ws://0.0.0.0:8080");

    ws.current.onmessage = (msg: MessageEvent<any>) => {
      const data = JSON.parse(msg.data);

      if (data.type === "scan_results") {
        // read shit
      }
    };

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
          // Extract the base URL (protocol + host)
          setBaseUrl(url.host);
        }
      } catch (error) {
        console.error("Failed to get the active tab's URL:", error);
      }
    };

    getBaseUrl();

    return () => {
      if (ws.current) {
        ws.current.close()
      }
    }
  }, []);

  return (
    <ThemeProvider defaultTheme="light">
      <TooltipProvider>
        <div className="flex flex-col gap-3 m-3 h-full ">
          <Card className="p-2">
            <CardTitle>
              <div className="flex items-center justify-between">
                <span className="p-2">Denis Defend</span>
                <div>
                  <img className="h-[2.5rem] w-auto" src={denisLogo} />
                </div>
              </div>
            </CardTitle>
          </Card>
          <Card
            style={{
              backgroundImage:
                "linear-gradient(to bottom right, rgb(182, 244, 146), rgb(255, 255, 255))",
              // (255, 8, 0)
            }}
          >
            <CardHeader>
              <CardTitle>
                <Tooltip>
                  <TooltipTrigger>
                    <div className="flex gap-2 items-center min-w-0">
                      {baseUrl ? baseUrl : "Loading..."}
                      <CircleCheck />
                    </div>
                  </TooltipTrigger>
                  <TooltipContent>
                    <p>Trust: 85%</p>
                  </TooltipContent>
                </Tooltip>
              </CardTitle>
              <CardDescription>last scan 10d ago</CardDescription>
            </CardHeader>
            <CardContent className="w-full"></CardContent>
            {/* <CardFooter>
          <p>Card Footer</p>
        </CardFooter> */}
          </Card>
          <Button
            onClick={() =>
              ws.current?.send(
                JSON.stringify({ type: "scan_request", url: "google.com" })
              )
            }
          >
            Rescan
          </Button>
        </div>
      </TooltipProvider>
    </ThemeProvider>
  );
  // return (
  //   <div className="flex flex-col align-center gap-3 m-3 h-full ">
  //     <h3 className="scroll-m-20 text-center text-2xl font-semibold tracking-tight">
  //       Denis Defend
  //     </h3>
  //     <Card>
  //       <CardHeader>
  //         <CardTitle>africagucci.com</CardTitle>
  //         <CardDescription>never scanned</CardDescription>
  //       </CardHeader>
  //       <CardContent className="w-full">
  //         <Button >Scan website</Button>
  //       </CardContent>
  //       {/* <CardFooter>
  //         <p>Card Footer</p>
  //       </CardFooter> */}
  //     </Card>
  //   </div>
  // );
}
