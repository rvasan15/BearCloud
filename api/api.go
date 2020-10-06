package api

import (
	"encoding/json"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"

	"fmt"
)

//Declare a global array of Credentials
//See credentials.go

/*YOUR CODE HERE*/
var credentials []Credentials = []Credentials{}

func RegisterRoutes(router *mux.Router) error {

	/*

		Fill out the appropriate get methods for each of the requests, based on the nature of the request.

		Think about whether you're reading, writing, or updating for each request


	*/

	router.HandleFunc("/api/getCookie", getCookie).Methods(http.MethodGet)
	router.HandleFunc("/api/getQuery", getQuery).Methods(http.MethodGet)
	router.HandleFunc("/api/getJSON", getJSON).Methods(http.MethodGet)

	router.HandleFunc("/api/signup", signup).Methods(http.MethodPost)
	router.HandleFunc("/api/getIndex", getIndex).Methods(http.MethodGet)
	router.HandleFunc("/api/getpw", getPassword).Methods(http.MethodGet)
	router.HandleFunc("/api/updatepw", updatePassword).Methods(http.MethodPut)
	router.HandleFunc("/api/deleteuser", deleteUser).Methods(http.MethodDelete)

	return nil
}

func getCookie(response http.ResponseWriter, request *http.Request) {

	/*
		Obtain the "access_token" cookie's value and write it to the response

		If there is no such cookie, write an empty string to the response
	*/

	/*YOUR CODE HERE*/

	cookie, err := request.Cookie("access_token")

	//check if obtaining the cookie returned an error
	if err != nil {
		fmt.Fprintf(response, "")
		return
	}

	//Get the value of the cookie we just obtained and print it out to the response output
	accessToken := cookie.Value
	fmt.Fprintf(response, accessToken)
	return
}

func getQuery(response http.ResponseWriter, request *http.Request) {

	/*
		Obtain the "userID" query paramter and write it to the response
		If there is no such query parameter, write an empty string to the response
	*/

	/*YOUR CODE HERE*/

	username := request.URL.Query().Get("userID")
	fmt.Fprintf(response, username)

}

func getJSON(response http.ResponseWriter, request *http.Request) {

	/*
		Our JSON file will look like this:

		{
			"username" : <username>,
			"password" : <password>
		}

		Decode this json file into an instance of Credentials.

		Then, write the username and password to the response, separated by a newline.request

		Make sure to error check! If there are any errors, call http.Error(), and pass in a "http.StatusBadRequest" What kind of errors can we expect here?
	*/

	/*YOUR CODE HERE*/

	// username := request.URL.Query().Get("username")
	// password := request.URL.Query().Get("password")

	//create an empty credential
	credentials := Credentials{}

	//create a new json decoder that will allow us to decode the request body
	jsonDecoder := json.NewDecoder(request.Body)

	//use our decoder to decode the contents of the request body into our credential
	err := jsonDecoder.Decode(&credentials)

	//Check if we got an error. If err != nil, that function returned an error
	if err != nil {
		http.Error(response, err.Error(), http.StatusBadRequest)
		return
	}

	fmt.Fprintf(response, credentials.Username+"\n")
	fmt.Fprintf(response, credentials.Password)
	return
}

func signup(response http.ResponseWriter, request *http.Request) {

	/*
		Our JSON file will look like this:

		{
			"username" : <username>,
			"password" : <password>
		}

		Decode this json file into an instance of Credentials.

		Then store it ("append" it) to the global array of Credentials.

		Make sure to error check! If there are any errors, call http.Error(), and pass in a "http.StatusBadRequest" What kind of errors can we expect here?
	*/

	/*YOUR CODE HERE*/

	//create a credential
	newCredentials := Credentials{}

	//take the credential in the request and move the contents to our credential
	err := json.NewDecoder(request.Body).Decode(&newCredentials)
	if err != nil {
		http.Error(response, err.Error(), http.StatusBadRequest)
		response.WriteHeader(201)
		return
	}

	credentials = append(credentials, newCredentials)

	return

}

func getIndex(response http.ResponseWriter, request *http.Request) {

	/*
		Our JSON file will look like this:

		{
			"username" : <username>
		}


		Decode this json file into an instance of Credentials. (What happens when we don't have all the fields? Does it matter in this case?)

		Return the array index of the Credentials object in the global Credentials array

		The index will be of type integer, but we can only write strings to the response. What library and function was used to get around this?

		Make sure to error check! If there are any errors, call http.Error(), and pass in a "http.StatusBadRequest" What kind of errors can we expect here?
	*/

	/*YOUR CODE HERE*/

	//create a credential
	newCredentials := Credentials{}
	//username := request.URL.Query().Get("username")
	//take the credential in the request and move the contents to our credential
	err := json.NewDecoder(request.Body).Decode(&newCredentials)
	if err != nil {
		http.Error(response, err.Error(), http.StatusBadRequest)
		return
	}

	//var index int

	for i, c := range credentials {

		if c.Username == newCredentials.Username {
			fmt.Fprintf(response, strconv.Itoa(i))
			break
		}
	}

	http.Error(response, "No such index exists", http.StatusBadRequest)

}

func getPassword(response http.ResponseWriter, request *http.Request) {

	/*
		Our JSON file will look like this:

		{
			"username" : <username>
		}


		Decode this json file into an instance of Credentials. (What happens when we don't have all the fields? Does it matter in this case?)

		Write the password of the specific user to the response

		Make sure to error check! If there are any errors, call http.Error(), and pass in a "http.StatusBadRequest" What kind of errors can we expect here?
	*/

	/*YOUR CODE HERE*/
	newCredentials := Credentials{}
	//username := request.URL.Query().Get("username")
	//take the credential in the request and move the contents to our credential
	err := json.NewDecoder(request.Body).Decode(&newCredentials)
	if err != nil {
		http.Error(response, err.Error(), http.StatusBadRequest)
		return
	}

	var password string

	for _, c := range credentials {

		if c.Username == newCredentials.Username {
			password = c.Password
			break
		}
	}

	fmt.Fprintf(response, password)
	return

}

func updatePassword(response http.ResponseWriter, request *http.Request) {

	/*
		Our JSON file will look like this:

		{
			"username" : <username>,
			"password" : <password,
		}


		Decode this json file into an instance of Credentials.

		The password in the JSON file is the new password they want to replace the old password with.

		You don't need to return anything in this.

		Make sure to error check! If there are any errors, call http.Error(), and pass in a "http.StatusBadRequest" What kind of errors can we expect here?
	*/

	/*YOUR CODE HERE*/

	newCredentials := Credentials{}
	// username := request.URL.Query().Get("username")
	// password := request.URL.Query().Get("password")

	//take the credential in the request and move the contents to our credential
	err := json.NewDecoder(request.Body).Decode(&newCredentials)
	if err != nil {
		http.Error(response, err.Error(), http.StatusBadRequest)
		return
	}

	for _, c := range credentials {

		if c.Username == newCredentials.Username {
			c.Password = newCredentials.Password
			break
		}
	}

}

func deleteUser(response http.ResponseWriter, request *http.Request) {

	/*
		Our JSON file will look like this:

		{
			"username" : <username>,
			"password" : <password,
		}


		Decode this json file into an instance of Credentials.

		Remove this user from the array. Preserve the original order. You may want to create a helper function.

		This wasn't covered in lecture, so you may want to read the following:
			- https://gobyexample.com/slices
			- https://www.delftstack.com/howto/go/how-to-delete-an-element-from-a-slice-in-golang/

		Make sure to error check! If there are any errors, call http.Error(), and pass in a "http.StatusBadRequest" What kind of errors can we expect here?
	*/

	/*YOUR CODE HERE*/

	newCredentials := Credentials{}
	//username := request.URL.Query().Get("username")

	//take the credential in the request and move the contents to our credential
	err := json.NewDecoder(request.Body).Decode(&newCredentials)
	if err != nil {
		http.Error(response, err.Error(), http.StatusBadRequest)
		return
	}

	for i, c := range credentials {

		if c.Username == newCredentials.Username {
			credentials = remove(credentials, i)
			break
		}
	}

	return
}

func remove(slice []Credentials, s int) []Credentials {
	return append(slice[:s], slice[s+1:]...)
}
