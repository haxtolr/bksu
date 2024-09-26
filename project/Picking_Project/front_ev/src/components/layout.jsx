// This is the root layout component for your Next.js app.
// Learn more: https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts#root-layout-required

import { Arimo } from 'next/font/google'
import { Cormorant_Garamond } from 'next/font/google'
import '../styles/styles.css'

const arimo = Arimo({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-arimo',
})
const cormorant_garamond = Cormorant_Garamond({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-cormorant_garamond',
})

export default function Layout({ children }) {
  return (
    <html lang="ko">
      <body className={arimo.variable + ' ' + cormorant_garamond.variable}>
        {children}
      </body>
    </html>
  )
}