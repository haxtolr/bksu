/**
* This code was generated by v0 by Vercel.
* @see https://v0.dev/t/YKpDYCIPuot
* Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
*/

/** Add fonts into your Next.js project:

import { Arimo } from 'next/font/google'
import { Cormorant_Garamond } from 'next/font/google'

arimo({
  subsets: ['latin'],
  display: 'swap',
})

cormorant_garamond({
  subsets: ['latin'],
  display: 'swap',
})

To read more about using these font, please visit the Next.js documentation:
- App Directory: https://nextjs.org/docs/app/building-your-application/optimizing/fonts
- Pages Directory: https://nextjs.org/docs/pages/building-your-application/optimizing/fonts
**/
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

export function Component() {
  return (
    (<div
      className="flex h-screen w-full items-center justify-center bg-[#e0e0ff] dark:bg-[#2a2a3e]">
      <div
        className="mx-4 w-full max-w-md space-y-6 rounded-lg bg-white p-6 shadow-lg dark:bg-[#3c3c4f]">
        <div className="flex items-center justify-center">
          <h1 className="text-3xl font-bold text-[#5b5b8c] dark:text-white">EV</h1>
        </div>
        <div className="space-y-4">
          <div>
            <Label className="text-[#5b5b8c] dark:text-white" htmlFor="username">
              Username
            </Label>
            <Input
              className="mt-1 w-full rounded-md border border-gray-200 border-[#d0d0e0] bg-[#f8f8f8] px-3 py-2 text-[#5b5b8c] placeholder:text-[#a0a0b0] focus:border-[#9090c0] focus:outline-none dark:border-[#606080] dark:bg-[#3c3c4f] dark:text-white dark:placeholder:text-[#808090] dark:border-gray-800"
              id="username"
              placeholder="Enter your username"
              type="text" />
          </div>
          <div>
            <Label className="text-[#5b5b8c] dark:text-white" htmlFor="password">
              Password
            </Label>
            <Input
              className="mt-1 w-full rounded-md border border-gray-200 border-[#d0d0e0] bg-[#f8f8f8] px-3 py-2 text-[#5b5b8c] placeholder:text-[#a0a0b0] focus:border-[#9090c0] focus:outline-none dark:border-[#606080] dark:bg-[#3c3c4f] dark:text-white dark:placeholder:text-[#808090] dark:border-gray-800"
              id="password"
              placeholder="Enter your password"
              type="password" />
          </div>
          <div className="space-y-2">
            <Button
              className="w-full rounded-md bg-[#9090c0] py-2 font-medium text-white hover:bg-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 dark:bg-[#707090] dark:hover:bg-[#606080] dark:focus:ring-[#707090]"
              type="submit">
              Login
            </Button>
            <div className="flex items-center justify-between">
              <Button
                className="text-[#9090c0] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 dark:text-[#707090] dark:hover:text-[#606080] dark:focus:ring-[#707090]"
                variant="link">
                Sign Up
              </Button>
            </div>
          </div>
          <div
            className="rounded-md bg-[#e0e0ff] p-4 text-[#5b5b8c] dark:bg-[#3c3c4f] dark:text-white">
            <p>Awaiting approval</p>
          </div>
          <div
            className="rounded-md bg-[#e0e0ff] p-4 text-[#5b5b8c] dark:bg-[#3c3c4f] dark:text-white">
            <p>Incorrect username or password</p>
          </div>
        </div>
      </div>
    </div>)
  );
}
