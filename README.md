
# JAP
JAP or job application platform as a medium to connect organizations with job applicants.
This program will processed the resume files and calculate the relevancy from the skills of the 
applicant to the skills required of each position and filter questions then sent a question suggestion list
to the organization admin to select the appropriate questions for that applicant.

How to run the program

Run each python files separately.

data-analysis
Create the following directories in the directories Filesys where the python code files are. 
This will act as the place to hold the files once it is processed.
1. ApplicantFolder
2. InboundResume
3. InboundTesseract
4. Scores
5. TempStation
6. TxtMapCleaned
7. TxtMapUncleaned
8. TxtQuesCleaned
9. TxtQuesImage
10. TxtQuesUncleaned

The code will extract the text twice, one using PDFminer and the other using Pytessaract.
Then each of the text files that were extracted will then trigger the set of codes to starts:
1. Extract skills then map with all available position and calculate the percentage match
2. Locate the text section from key words in header list then extract skills
   group the skills into difficulty levels then map with the existed question in database
=======
This is the final year project for Computer Innovation Engineering at KMITL

## Build Setup

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

For detailed explanation on how things work, check out the [documentation](https://nuxtjs.org).

## Special Directories

You can create the following extra directories, some of which have special behaviors. Only `pages` is required; you can delete them if you don't want to use their functionality.

### `assets`

The assets directory contains your uncompiled assets such as Stylus or Sass files, images, or fonts.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/assets).

### `components`

The components directory contains your Vue.js components. Components make up the different parts of your page and can be reused and imported into your pages, layouts and even other components.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/components).

### `layouts`

Layouts are a great help when you want to change the look and feel of your Nuxt app, whether you want to include a sidebar or have distinct layouts for mobile and desktop.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/layouts).


### `pages`

This directory contains your application views and routes. Nuxt will read all the `*.vue` files inside this directory and setup Vue Router automatically.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/get-started/routing).

### `plugins`

The plugins directory contains JavaScript plugins that you want to run before instantiating the root Vue.js Application. This is the place to add Vue plugins and to inject functions or constants. Every time you need to use `Vue.use()`, you should create a file in `plugins/` and add its path to plugins in `nuxt.config.js`.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/plugins).

### `static`

This directory contains your static files. Each file inside this directory is mapped to `/`.

Example: `/static/robots.txt` is mapped as `/robots.txt`.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/static).

### `store`

This directory contains your Vuex store files. Creating a file in this directory automatically activates Vuex.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/docs/2.x/directory-structure/store).
