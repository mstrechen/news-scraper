# news-scrapper
News scrapper from different sources written on Python3


##### Dev plan:
- **Make basic http server with request handling**
    - [x] Static content handling
    - [x] GET dynamic methods handling
- **UI**
    - [x] Basic UI for getting latest news
    - [ ] Sorting by tags interface
    - [x] Searching interface
    - [ ] Updating data interface 
    - [ ] Prettify
- **Database**
    - [x] Configure ElasticSearch
    - [ ] Configure filesystem for storing images
    - [x] Basic operations (inserting, extracting by limit and offset)
    - [ ] Extracting by tags
    - [ ] Complex operation (extracting by search query, fuzzy search)
- **Scrapper**
    - [ ] Basic scraper classes
    - [ ] Runing in different threads
    - [ ] Scrapping newslist
        - [ ] TSN.ua
        - [ ] ukr.net/ua (also try to fix datetime)
    - [ ] Scrapping full text of articles
        - [ ] TSN.ua
        - [ ] different sources of ukr.net:
            - [ ] internetua
            - [ ] depo.ua
            

    