

package org.springframework.RoostTest; // Ensure this package exists

import io.restassured.RestAssured; // Ensure this dependency is included in your project
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
import org.json.JSONObject; // Ensure this dependency is included in your project
import org.json.XML;
import org.json.JSONException;
import org.json.JSONArray;
import java.util.Arrays;

public class userUsernameDeleteTest {

	List<Map<String, String>> envList = new ArrayList<>();

	@BeforeEach
	public void setUp() {
		TestdataLoader dataloader = new TestdataLoader(); // Ensure this class and its methods are defined in your project
		String[] envVarsList = { "username" };
		envList = dataloader.load("src\\test\\java\\org\\springframework\\RoostTest\\user_usernameDeleteTest.csv",
				envVarsList);
	}

	@Test
	public void userUsernameDelete_Test() throws JSONException {
		this.setUp();
		Integer testNumber = 1;
		for (Map<String, String> testData : envList) {
			RestAssured.baseURI = (testData.get("BASE_URL") != null && !testData.get("BASE_URL").isEmpty())
					? testData.get("BASE_URL") : "https://petstore.swagger.io/v2";

			Response responseObj = given()
				.pathParam("username", testData.get("username") != null ? testData.get("username") : "")
				.when()
				.delete("/user/{username}")
				.then()
				.extract()
				.response();
			JsonPath response;
			String contentType = responseObj.getContentType();

			System.out.printf("Test Case %d: userUsernameDelete_Test \n", testNumber++);
			System.out.println("Request: DELETE /user/{username}");
			System.out.println("Status Code: " + responseObj.statusCode());
			if (testData.get("statusCode") != null) {
				String statusCodeFromCSV = testData.get("statusCode");
				if (statusCodeFromCSV.contains("X")) {
					MatcherAssert.assertThat(
							"Expected a status code of category " + statusCodeFromCSV + ", but got "
									+ Integer.toString(responseObj.statusCode()) + " instead",
							Integer.toString(responseObj.statusCode()).charAt(0), equalTo(statusCodeFromCSV.charAt(0)));
				}
				else {
					MatcherAssert.assertThat(Integer.toString(responseObj.statusCode()), equalTo(statusCodeFromCSV));
				}
			}
			else {
				List<Integer> expectedStatusCodes = Arrays.asList(400, 404);
				MatcherAssert.assertThat(responseObj.statusCode(), is(in(expectedStatusCodes)));
			}
			String stringifiedStatusCode = Integer.toString(responseObj.statusCode());
			if (contentType.contains("application/xml") || contentType.contains("text/xml")) {
				String xmlResponse = responseObj.asString();
				JSONObject jsonResponse = XML.toJSONObject(xmlResponse);
				JSONObject jsonData = jsonResponse.getJSONObject("xml");
				String jsonString = jsonData.toString();
				response = new JsonPath(jsonString);

			}
			else if (contentType.contains("application/json")) {
				response = responseObj.jsonPath();
			}
			else {
				System.out.println("Response content type found: " + contentType
						+ ", but RoostGPT currently only supports the following response content types: application/json,text/xml,application/xml");
				continue;
			}

			if (stringifiedStatusCode.equals("400")) {
				System.out.println("Description: Invalid username supplied");
			}
			if (stringifiedStatusCode.equals("404")) {
				System.out.println("Description: User not found");
			}

		}
	}

}
