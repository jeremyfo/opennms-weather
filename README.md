# weather.py

OpenNMS http://opennms.org is the world’s first enterprise grade network management application platform developed under the open source model. This python script will display weather data on the home page 'index.jsp' and can be run from a cronjob.

## Install
1. Setup a developer api key on wunderground http://www.wunderground.com/weather/api
2. Edit 'weather.py' add your API_KEY and change your location
3. Copy weather.py to '/opt/opennms/bin'
4. Create a cronjob that will run the weather.py script periodically '\*/10 \* \* \* \* /bin/python /opt/opennms/bin/weather.py > /dev/null 2>&1'
5. Edit '/opt/opennms/jetty-webapps/opennms/index.jsp' and add the below block of code.
```
<!-- Right Column -->
        <div class="col-md-3" id="index-contentright">
                <!-- weather box -->
                <jsp:include page="/includes/weather.jsp" flush="false" />
```
## Screenshot