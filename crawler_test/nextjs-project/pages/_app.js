// top-level component - common across pages
// use this to keep state when navigating
import '../styles/global.css'

export default function App({ Component, pageProps }) {
    return <Component {...pageProps} />
}