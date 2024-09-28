import "../styles/globals.css";
import { Button } from "@/components/ui/button";
import { CircleCheck } from 'lucide-react';
import { Shield } from "lucide-react";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { ThemeProvider } from "@/components/theme-provider";

export default function () {
  return (
    <ThemeProvider defaultTheme="light">
      <div className="flex flex-col align-center gap-3 m-3 h-full ">
        <h3 className="scroll-m-20 text-center text-2xl font-semibold tracking-tight">
          Denis Defend
        </h3>
        <Card
          style={{
            backgroundImage:
              "linear-gradient(to bottom right, rgb(182, 244, 146), rgb(255, 255, 255))",
          }}
        >
          <CardHeader>
            <CardTitle>
              <div className="flex gap-2 align-center">
                goglle.com
                <CircleCheck />
              </div>
              </CardTitle>
            <CardDescription>last scan 10d ago</CardDescription>
          </CardHeader>
          <CardContent className="w-full">
          </CardContent>
          {/* <CardFooter>
          <p>Card Footer</p>
        </CardFooter> */}
        </Card>
        <Button>Rescan</Button>
      </div>
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
