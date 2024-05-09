

@Test
    public void petFindByTagsGet_Test() throws JSONException {
        this.setUp();
        Integer testNumber = 1;
        for (Map<String, String> testData : envList) {
          RestAssured.baseURI = (testData.get("BASE_URL") != null && !testData.get("BASE_URL").isEmpty()) ? testData.get("BASE_URL"): "https://petstore.swagger.io/v2";

                Response responseObj = given()
                .when()
                .get("/pet/findByTags")
                .then()
                .extract().response(); // --> Found an issue while compiling the code at this line. 'undefined' after given() method is not a valid syntax in RestAssured. Commenting this line would result in a compilation error, as "given().undefined" is a syntax error. The 'undefined' should be replaced by a request specification or removed if not required.

              JsonPath response;
              String contentType = responseObj.getContentType();

              System.out.printf("Test Case %d: petFindByTagsGet_Test \n", testNumber++);
              System.out.println("Request: GET /pet/findByTags");
              System.out.println("Status Code: " + responseObj.statusCode());
             //... rest code
}
