

package org.springframework.RoostTest;

import io.restassured.RestAssured;
import io.restassured.path.json.JsonPath;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.given;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;
import org.hamcrest.MatcherAssert;
import static org.hamcrest.Matchers.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.json.JSONObject;
import org.json.XML;
import org.json.JSONException;
import org.json.JSONArray;
import java.util.Arrays;

public class petPutTest {

	List<Map<String, String>> envList = new ArrayList<>();

	@BeforeEach
	public void setUp() {
		TestdataLoader dataloader = new TestdataLoader();
		String[] envVarsList = { "" };
		envList = dataloader.load("src\\test\\java\\org\\springframework\\RoostTest\\petPutTest.csv", envVarsList);
	}

	@Test
    public void petPut_Test() throws JSONException {
        this.setUp();
        Integer testNumber = 1;
        for (Map<String, String> testData : envList) {
          RestAssured.baseURI = (testData.get("BASE_URL") != null && !testData.get("BASE_URL").isEmpty()) ? testData.get("BASE_URL"): "https://petstore.swagger.io/v2";

                Response responseObj = given().when().put("/pet").then().extract().response(); // Corrected line
              JsonPath response;
              String contentType = responseObj.getContentType();

              System.out.printf("Test Case %d: petPut_Test \n", testNumber++);
              System.out.println("Request: PUT /pet");
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
              				else {
      List<Integer> expectedStatusCodes = Arrays.asList(400,404,405);
				MatcherAssert.assertThat(responseObj.statusCode(), is(in(expectedStatusCodes)));
          }
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

                if(stringifiedStatusCode.equals("400")){					System.out.println("Description: Invalid ID supplied");
				}
if(stringifiedStatusCode.equals("404")){					System.out.println("Description: Pet not found");
				}
if(stringifiedStatusCode.equals("405")){					System.out.println("Description: Validation exception");
				}


            }
    }

}
