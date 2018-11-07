import urllib2, base64, ssl
import requests, json

username = 'isadmin'
password = 'isadmin'
# http_url='https://cap-sg-prd-4.integration.ibmcloud.com:16217/ibm/iis/igc-rest/v1/bundles/assets'
#http_url = 'https://fiocchi-master-1.fyre.ibm.com:30924/ibm/iis/igc-rest/v1/bundles/assets'

post_asset_url  = 'http://9.30.42.133:8888/v1/assets'

post_custom_asset_url = 'http://9.30.42.133:8888/v1/bundles/assets'

# POST ASSET DATA
def post_asset(http_url, username, password, xml_data):
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    request = urllib2.Request(url=http_url, data=xml_data, headers={'Content-Type': 'application/json'})


    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request, context=gcontext)
    print xml_data
    result.read()
    return result.read()



category_data = '{ "asset_name": "Sales Analytics 2","asset_type": "category","is_custom_asset": false}'

term_data = '{"asset_name": "Sales Reporting","asset_type": "term", "is_custom_asset": false, "custom_properties": {"category_name": "Sales Analytics","status": "ACCEPTED"}}'

associate_assets_url = 'http://9.30.42.133:8888/v1/relatedAssets'

associate_xml = '{ "asset_name": "Sales Reporting", "asset_type": "term", "related_asset_name": "Oozie Workflow 1", "related_asset_type": "$Map_Reduce-AssetClass_2" }'

host_data =     '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                <doc xmlns="http://www.ibm.com/iis/flow-doc">
	            <assets>
	            <asset class="$Map_Reduce-AssetClass_1" repr="Host1" ID="w1">
                <attribute name="name" value="Host1" /><attribute name="short_description" value="Host 1" />
		        <attribute name="$ASSET_CLASS1_ATTR2_ID" value="3" />
                </asset></assets><importAction partialAssetIDs="w1" /></doc>'''

workflow_data =     '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                    <doc xmlns="http://www.ibm.com/iis/flow-doc">
	                <assets>
	                <asset class="$Map_Reduce-AssetClass_2" repr="Oozie Workflow 1" ID="w1">
                    <attribute name="name" value="Oozie Workflow 1" /><attribute name="short_description" value="Oozie " />
		            <attribute name="$ASSET_CLASS2_ATTR1_ID" value="WF1" />
		
                    <reference name="$AssetClass_1" assetIDs="parent_0" />
                    </asset>
                    <asset class ="$Map_Reduce-AssetClass_1" repr="Host1" ID="parent_0">
                    <attribute name="name" value="Host1" />
                    </asset></assets><importAction partialAssetIDs="parent_0" /></doc>'''


mapper_1_data =     '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                    <doc xmlns="http://www.ibm.com/iis/flow-doc">
	                <assets>
	                <asset class="$Map_Reduce-AssetClass_3" repr="Mapper 1" ID="w1">
                    <attribute name="name" value="Mapper 1" />
                    <attribute name="long_description" value="Map function to get the PID, Sales and partition them by PID" />
	                <attribute name="$ASSET_CLASS3_ATTR2_ID" value="mapper_sales.py" />
	                <reference name="$AssetClass_2" assetIDs="parent_1" />
                    </asset>
                    <asset class ="$Map_Reduce-AssetClass_2" repr="Oozie Workflow 1" ID="parent_1">
                    <attribute name="name" value="Oozie Workflow 1" />
                    <reference name="$AssetClass_1" assetIDs="parent_0" />
                    </asset>

                    <asset class ="$Map_Reduce-AssetClass_1" repr="Host1" ID="parent_0">
                    <attribute name="name" value="Host1" />
                    </asset>
                    </assets>
                    <importAction partialAssetIDs="parent_0" /></doc>'''


mapper_2_data =     '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                      <doc xmlns="http://www.ibm.com/iis/flow-doc">
                        <assets>
                        <asset class="$Map_Reduce-AssetClass_3" repr="Mapper 2" ID="w1">
                        <attribute name="name" value="Mapper 2" />
                        <attribute name="long_description" value="Join the aggregated sales amount by person in the step above and get the sales person name so it is better for reporting." />
                        <attribute name="$ASSET_CLASS3_ATTR2_ID" value="mapper_report.py" />
                        <reference name="$AssetClass_2" assetIDs="parent_1" />
                        </asset>
                        <asset class ="$Map_Reduce-AssetClass_2" repr="Oozie Workflow 1" ID="parent_1">
                        <attribute name="name" value="Oozie Workflow 1" />
                        <reference name="$AssetClass_1" assetIDs="parent_0" />
                        </asset>
                    
                        <asset class ="$Map_Reduce-AssetClass_1" repr="Host1" ID="parent_0">
                        <attribute name="name" value="Host1" />
                        </asset>
                        </assets>
                        <importAction partialAssetIDs="parent_0" /></doc>'''

reducer_1_data =      '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                        <doc xmlns="http://www.ibm.com/iis/flow-doc">
                            <assets>
                            <asset class="$Map_Reduce-AssetClass_4" repr="Reducer 1" ID="w1">
                        <attribute name="name" value="Reducer 1" />
                        <attribute name="short_description" value="Short Desc : Take the sorted/partitioned sales figures by Person and aggregate (sum) the values to get total sales amount by Person ID" />
                        <attribute name="long_description" value="Long Desc : Take the sorted/partitioned sales figures by Person and aggregate (sum) the values to get total sales amount by Person ID" />
                        <attribute name="$ASSET_CLASS4_ATTR1_ID" value="\\usr\\bin\\" />
                        <attribute name="$ASSET_CLASS4_ATTR2_ID" value="reducer_sales.py" />
                        <reference name="$AssetClass_2" assetIDs="parent_1" />
                            </asset>
                            <asset class ="$Map_Reduce-AssetClass_2" repr="Oozie Workflow 1" ID="parent_1">
                            <attribute name="name" value="Oozie Workflow 1" />
                            <reference name="$AssetClass_1" assetIDs="parent_0" />
                            </asset>
                        
                            <asset class ="$Map_Reduce-AssetClass_1" repr="Host1" ID="parent_0">
                            <attribute name="name" value="Host1" />
                            </asset>
                            </assets>
                            <importAction partialAssetIDs="parent_0" /></doc>'''


# Create Category : Sales Analytics
post_asset(post_asset_url, username, password, category_data)

# Create Term : Sales Reporting
post_asset(post_asset_url, username, password, term_data)

#Creating custom asset instances
# A. Create Host
post_asset(post_custom_asset_url, username, password, host_data)

# B. Create Workflow
post_asset(post_custom_asset_url, username, password, workflow_data)

# C. Create Mapper 1
post_asset(post_custom_asset_url, username, password, mapper_1_data)

# D. Create Reducer 1
post_asset(post_custom_asset_url, username, password, reducer_1_data)

# E. Create Mapper 2
post_asset(post_custom_asset_url, username, password, mapper_2_data)

# Associate Sales Reporting to the Workflow
post_asset(associate_assets_url, username, password, associate_xml)



