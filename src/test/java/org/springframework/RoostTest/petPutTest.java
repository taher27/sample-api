

@Test
public void petPut_Test() throws JSONException {
    this.setUp();
    Integer testNumber = 1;
    for (Map<String, String> testData : envList) {
		RestAssured.baseURI = (testData.get("BASE_URL") != null && !testData.get("BASE_URL").isEmpty()) ? testData.get("BASE_URL"): "https://petstore.swagger.io/v2";

		// Syntax error on the line below, 'given()' method needs to be either assigned or included as part of an expression
		// Fixing the syntax error 
		Response responseObj = given().contentType(ContentType.JSON)
		.when()
		.put("/pet")
		.then()
		.extract().response();
		// code continues...
