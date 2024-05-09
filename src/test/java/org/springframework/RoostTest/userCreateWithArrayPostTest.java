

@Test
public void userCreateWithArrayPost_Test() throws JSONException {
    this.setUp();
    Integer testNumber = 1;
    for (Map<String, String> testData : envList) {
      RestAssured.baseURI = (testData.get("BASE_URL") != null && !testData.get("BASE_URL").isEmpty()) ? testData.get("BASE_URL"): "https://petstore.swagger.io/v2";

            Response responseObj = given()
            .header("body", testData.get("body") != null ? testData.get("body") : "")
            .when()
            .post("/user/createWithArray")
            .then()
            .extract().response();
          JsonPath response;
          String contentType = responseObj.getContentType();

          System.out.printf("Test Case %d: userCreateWithArrayPost_Test \n", testNumber++);
          System.out.println("Request: POST /user/createWithArray");
          System.out.println("Status Code: " + responseObj.statusCode());
          if (testData.get("statusCode") != null) {
            String statusCodeFromCSV = testData.get("statusCode");
            if (statusCodeFromCSV.contains("X")) {
              MatcherAssert.assertThat(
                  "Expected a status code of category " + statusCodeFromCSV + ", but got "
                      + Integer.toString(responseObj.statusCode()) + " instead",
                  Integer.toString(responseObj.statusCode()).charAt(0), equalTo(statusCodeFromCSV.charAt(0)));
            } else {
              MatcherAssert.assertThat(
                  Integer.toString(responseObj.statusCode()), equalTo(statusCodeFromCSV));
            }
          }
          // Commenting out the below code as it has compilation errors.
          // The variable 'default' is not defined and cannot be used in this context.
          /*
          else {
              List<Integer> expectedStatusCodes = Arrays.asList(default);
              MatcherAssert.assertThat(responseObj.statusCode(), is(in(expectedStatusCodes)));
          }
          */
          String stringifiedStatusCode = Integer.toString(responseObj.statusCode());
          if (contentType.contains("application/xml") || contentType.contains("text/xml")) {
            String xmlResponse = responseObj.asString();
            JSONObject jsonResponse = XML.toJSONObject(xmlResponse);
            JSONObject jsonData = jsonResponse.getJSONObject("xml");
            String jsonString = jsonData.toString();
            response = new JsonPath(jsonString);

          } else if(contentType.contains("application/json")){
            response = responseObj.jsonPath();
          } else {
            System.out.println("Response content type found: "+contentType+", but RoostGPT currently only supports the following response content types: application/json,text/xml,application/xml");
            continue;
          }

          // Commenting out the below code as it has compilation errors.
          // The string 'default' cannot be equated with an integer value.
          /*
          if(stringifiedStatusCode.equals("default")){                   
              System.out.println("Description: successful operation");
          }
          */


        }
}
