# news-scraper
News scraper from different sources written on Python3


##### Dev plan:
- **Make basic http server with request handling**
    - [x] Static content handling
    - [x] GET dynamic methods handling
- **UI**
    - [x] Basic UI for getting latest news
    - [x] Sorting by tags interface
    - [x] Searching interface
    - [x] Updating data interface 
    - [ ] Prettify
- **Database**
    - [x] Configure ElasticSearch
    - [x] Configure filesystem for storing images
    - [x] Basic operations (inserting, extracting by limit and offset)
    - [x] Extracting by tags
    - [x] Complex operation (extracting by search query, fuzzy search)
- **Scraper**
    - [x] Basic scraper classes
    - [x] Runing in different threads
    - [x] Scraping newslist
        - [x] TSN.ua
        - [x] ukr.net/ua (also try to fix datetime)
    - [x] Scrpping full text of articles
        - [x] TSN.ua
        - [x] different sources of ukr.net:
            - [x] internetua
            - [x] uabanker
- **Deploying**
    - [ ] configure docker-compose.yml
    - [ ] deploy on cloud

            

    