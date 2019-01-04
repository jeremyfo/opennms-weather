## Weather Underground API is no longer free - https://apicommunity.wunderground.com/weatherapi/topics/end-of-service-for-the-weather-underground-api.

## Please see a new version of this script that uses weather.gov api. https://github.com/jeremyfo/opennms-weather-v2

# weather.py

[OpenNMS](http://opennms.org) is the world’s first enterprise grade network management application platform developed under the open source model. This python script will display weather data and a radar map on the OpenNMS home page.

## Install
1. Setup a developer api key on wunderground http://www.wunderground.com/weather/api
2. Edit `weather.py` add your API_KEY and change your location in the URLs
3. Copy `weather.py` to `/opt/opennms/bin`
4. Create a cronjob that will run the `weather.py` script `*/10 * * * * /bin/python /opt/opennms/bin/weather.py > /dev/null 2>&1`
5. Edit `/opt/opennms/jetty-webapps/opennms/index.jsp` and add the below block of code to the appropriate column.
```
<!-- weather box -->
<jsp:include page="/includes/weather.jsp" flush="false" />
```
To add the weather panel to the top of the right column the code would look like
```
<!-- Right Column -->
        <div class="col-md-3" id="index-contentright">
                <!-- weather box -->
                <jsp:include page="/includes/weather.jsp" flush="false" />
```
## Screenshot
![weather.py screenshot](https://raw.githubusercontent.com/jeremyfo/opennms-weather/master/SCREENSHOT.PNG)

## Issues
This script has been tested against OpenNMS Horizon 16 and Horizon 17. After each OpenNMS upgrade you will need to add the code block back to `index.jsp`

Please report issues on the issue tracker or contact jeremyfo@gmail.com

## FAQ
**How do you set the size and radius of the Radar Image?**
In order to modify the radius and size of the radar image modify `radar_req_url` and set the width, height, and radius in the URL.
Example: `...width=450&height=450&radius=100`

**Where can I find more information about weather.py?**
[Tarus Balog's Blog Post](https://www.adventuresinoss.com/2016/02/01/add-a-weather-widget-to-opennms-home-screen)
