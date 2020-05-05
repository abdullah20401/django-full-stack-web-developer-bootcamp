var FirstName = prompt("Hello and Welcome. Please enter your first name:");
var LastName = prompt("Please enter your Last Name:");
var Age = prompt("How old are you?");
var Height = prompt("How tall are you in centimeters?");
var PetName = prompt("What is the name of your pet?");
alert("Thank you so much for the information.")

if (FirstName[0]===LastName[0] && Age>20&&Age<30 && Height>=170 && PetName[PetName.length - 1] === "y") {
  console.log("Welcome Comrade! You've passed the Spy Test");
} else {
  console.log("Sorry, nothing to see here.");
}
