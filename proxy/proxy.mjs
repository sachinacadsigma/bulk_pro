import { initializeAuthProxy } from '@propelauth/auth-proxy'

// Replace with your configuration
await initializeAuthProxy({
    authUrl: "https://2773068.propelauthtest.com",
    integrationApiKey: "d1f1bf70ad103bc363c4c6513d9f15b2a77dce848ef2bb0f54be1e33fedefbf5533584ccb8b933f892270f9754c12cb6",
    proxyPort: 8000,
    urlWhereYourProxyIsRunning: 'http://localhost:8000',
    target: {
        host: 'localhost',
        port: 8501,
        protocol: 'http:'
    },
})
