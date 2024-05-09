

Response responseObj = given()undefined.when()
                .post("/pet/{petId}/uploadImage")
                .then()
                .extract().response();
