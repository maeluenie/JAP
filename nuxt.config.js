import colors from 'vuetify/es5/util/colors'

export default {
    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        titleTemplate: '%s | JAP',
        title: 'Job Application Platform',
        htmlAttrs: {
            lang: 'en'
        },
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
        ]
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
        // https://go.nuxtjs.dev/vuetify
        '@nuxtjs/vuetify',
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        '@nuxtjs/axios',
        '@nuxtjs/auth-next'
    ],

    axios: {
        baseURL: 'https://api.job-application.duckdns.org'
      },
    // router:{
    //   middleware:['auth']
    // },
    auth:{
    redirect:{
        login:'/',
        logout:'/',
        home:'/',
    },
      strategies:{
        local: {
          token:{
            property: 'accessToken',
            type: ''
          },
          endpoints:{
            user: {
              property: false, // here should be `false`, as you defined in user endpoint `propertyName`
              autoFetch: true
            },
            login: { 
              headers: { 'Content-Type': 'application/json' },
              url: '/login', 
              method: 'post',  
              propertyName: 'accessToken'
            },
            logout: {
              headers: { 'Content-Type': 'application/json' },
              url: '/logout',
              method: 'delete'
            },
            user:{
              url: '/userinfo', 
              method: 'get', 
              propertyName: 'user'
            },
          },
          cookie: {
            options: {
              secure: false
             }
            }
        }
      }
    },
// auth: {
//     strategies: {
//         'local': {
//             scheme: 'refresh',
//             localStorage: {
//                 prefix: 'auth.'
//             },
//             token: {
//                 prefix: 'access_token.',
//                 property: 'access_token',
//                 maxAge: 86400,
//                 type: 'Bearer'
//             },
//             refreshToken: {
//                 prefix: 'refresh_token.',
//                 property: 'refresh_token',
//                 data: 'refresh_token',
//                 maxAge: 60 * 60 * 24 * 15
//             },
//             user: {
//                 property: 'user',
//                 autoFetch: true
//             },
//             endpoints: {
//                 login: { url: '/login', method: 'post'},
//                 refresh: { url: '/token/refresh/', method: 'post' },
//                 user: { url: '/userinfo', method: 'get' },
//                 logout: { url: '/logout', method: 'post'}
//             },
//                 }
//         }
//         },  

    // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
    vuetify: {
        customVariables: ['~/assets/variables.scss'],
        theme: {
            light: true,
            themes: {
                light: {
                    primary: colors.blue.darken2,
                    accent: colors.grey.darken3,
                    secondary: colors.amber.darken3,
                    info: colors.teal.lighten1,
                    warning: colors.amber.base,
                    error: colors.deepOrange.accent4,
                    success: colors.green.accent3
                }
            }
        }
    },

    

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {}
}