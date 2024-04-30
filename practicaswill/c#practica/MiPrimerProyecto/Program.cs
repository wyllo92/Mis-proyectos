// Random dice = new Random();

// int roll1 = dice.Next(1, 7);
// int roll2 = dice.Next(1, 7);
// int roll3 = dice.Next(1, 7);

// int total = roll1 + roll2 + roll3;

// Console.WriteLine($"Dice roll: {roll1} + {roll2} + {roll3} = {total}");

// if (roll1 == roll2 || roll1 == roll3 || roll2 == roll3)
// {
//     if ((roll1 == roll2) && (roll2 == roll3))

//     {
//         Console.WriteLine("You rolled triples! +6 bonus to total!");
//         total += 6;
//     }
//     else
//     {
//         Console.WriteLine("You rolled Doubles! +2 bonus to total!");
//         total += 2;
//     }
//     Console.WriteLine($"Your total including the bonus: {total}");
// }

// if (total >= 16)
// {
//     Console.WriteLine("You win a new car!");
// }
// else if (total >= 10)
// {
//     Console.WriteLine("You win a new laptop!");
// }
// else if (total >= 7)
// {
//     Console.WriteLine("You win a trip for two!");
// }
// else
// {
//     Console.WriteLine("You win a kitten!");
// }

// Random random = new Random();
// int daysUntilExpiration = random.Next(12);
// int discountPercentage = 0;

// if (daysUntilExpiration == 0)
// {
//     Console.WriteLine("Your subscription has expired.");
// }
// if (daysUntilExpiration == 1)
// {
//     Console.WriteLine("Your subscription expires within a day!");
// }
// else if (daysUntilExpiration <= 5)
// {
//     Console.WriteLine($"your subcription expires in {daysUntilExpiration} days");
// }
// else if (daysUntilExpiration <= 10)
// {
//     Console.WriteLine("Your subscription will expire soon. Renew Now!");
// }


// if (daysUntilExpiration == 1)
// {
//     discountPercentage = 20;
//     Console.WriteLine($"Renew now and save {discountPercentage}%!");
// }

// else if (daysUntilExpiration <= 5)
// {
//     discountPercentage = 10;
//     Console.WriteLine($"renew now and get {discountPercentage}%!");
// }


// Matrices-arrays 
/*
string[] fraudulentOrderIDs = new string[3];

fraudulentOrderIDs[0] = "A123";
fraudulentOrderIDs[1] = "B456";
fraudulentOrderIDs[2] = "C789";
// fraudulentOrderIDs[3] = "D000";
*/


// string [] fraudulentOrderIDs = {"A123", "B456", "C789"};

// Console.WriteLine($"First: {fraudulentOrderIDs[0]}");
// Console.WriteLine($"Second: {fraudulentOrderIDs[1]}");
// Console.WriteLine($"Third: {fraudulentOrderIDs[2]}");

// fraudulentOrderIDs[0] = "f000";
// Console.WriteLine($"Reassign first: {fraudulentOrderIDs[0]}");

// Console.WriteLine($"There are {fraudulentOrderIDs.Length} fraudulents orders to process");



//ej2
// int [] inventory = { 200, 450, 700, 175, 250 };
// int sum = 0;
// int bin = 0;

// foreach (int items in inventory)
// {
//     bin++;
//     sum += items;
//     Console.WriteLine($"Bin {bin} = {items} items (Running total: {sum})");
// }

// Console.WriteLine($"we have {sum} items in the inventory");

// string[] orders = { "B123", "C234", "A345", "C15", "B177", "G3003", "C235", "B179" };

// foreach (string order in orders)
// {
//     if (order.StartsWith('B'))
//     {
//         Console.WriteLine(order);
//     }
// }

//for and foreach
// Random random = new Random();
// string[] orderIDs = new string[5];

// for (int i = 0; i < orderIDs.Length; i++)
// {
//     int prefixValue = random.Next(65, 70);

//     string prefix = Convert.ToChar(prefixValue).ToString();

//     string suffix = random.Next(1, 1000).ToString("000");

//     orderIDs[i] = prefix + suffix;
// }
// foreach (var orderID in orderIDs)
// {
//     Console.WriteLine(orderID);
// }

/* this code show in console the reverse message and then shows how many "o" there are in the message*/
// string message = "The quick brown fox jumps over the lazy dog.";
// char[] lettersOfMessage = message.ToCharArray();
// int number = 0;

// Array.Reverse(lettersOfMessage);

// foreach (char letter in lettersOfMessage)
// {
//     if (letter == 'o')
//     {
//         number++;
//     }
// }

// string newMessage = new String(lettersOfMessage);

// Console.WriteLine(newMessage);
// Console.WriteLine($"'o' appears {number} times.");






//codigo que muestra a los alumnos su calificacion en letra y numero, hacer un foreach anidado y varios if else
// int examAssignments = 5;

// int[] sophiaScores = new int[] { 90, 86, 87, 98, 100, 94, 90 };
// int[] andrewScores = new int[] { 92, 89, 81, 96, 90, 89 };
// int[] emmaScores = new int[] { 90, 85, 87, 98, 68, 89, 89, 89 };
// int[] loganScores = new int[] { 90, 95, 87, 88, 96, 96 };
// int[] beckyScores = [92, 91, 90, 91, 92, 92, 92];
// int[] chrisScores = [84, 86, 88, 90, 92, 94, 96, 98];
// int[] ericScores = [80, 90, 100, 80, 90, 100, 80, 90];
// int[] gregorScores = [91, 91, 91, 91, 91, 91, 91];

// // Student names
// string[] studentNames = new string[] {"Sophia", "Andrew", "Emma", "Logan", "Becky", "Chris", "Eric", "Gregor"};

// int[] studentScores = new int[10];

// string currentStudentLetterGrade = "";

// // Display the Report Header
// Console.WriteLine("Student\t\tGrade\n");

// foreach (string name in studentNames)
// {
//     string currentStudent = name;

//     if (currentStudent == "Sophia")
//         // assign Sophia's scores to the studentScores array 
//         studentScores = sophiaScores;

//     else if (currentStudent == "Andrew")
//         // assign Andrew's scores to the studentScores array 
//         studentScores = andrewScores;

//     else if (currentStudent == "Emma")
//         // assign Emma's scores to the studentScores array 
//         studentScores = emmaScores;

//     else if (currentStudent == "Logan")
//         studentScores = loganScores;

//     else if (currentStudent == "Becky")
//         studentScores = beckyScores;

//     else if (currentStudent == "Chris")
//         studentScores = chrisScores;

//     else if (currentStudent == "Eric")
//         studentScores = ericScores;

//     else if (currentStudent == "Gregor")
//         studentScores = gregorScores;

//     else 
//         continue;

//     // initialize/reset the sum of scored assignments
//     int sumAssignmentScores = 0;

//     // initialize/reset the calculated average of exam + extra credit scores
//     decimal currentStudentGrade = 0;

//     int gradedAssignments = 0;

//     foreach (int score in studentScores)
//     {
//         gradedAssignments += 1;

//         if (gradedAssignments <= examAssignments)

//             sumAssignmentScores += score;
//         else

//             sumAssignmentScores += score / 10;

//     }

//     currentStudentGrade = (decimal)(sumAssignmentScores) / examAssignments;

//     if (currentStudentGrade >= 97)
//         currentStudentLetterGrade = "A+";

//     else if (currentStudentGrade >= 93)
//         currentStudentLetterGrade = "A";

//     else if (currentStudentGrade >= 90)
//         currentStudentLetterGrade = "A-";

//     else if (currentStudentGrade >= 87)
//         currentStudentLetterGrade = "B+";

//     else if (currentStudentGrade >= 83)
//         currentStudentLetterGrade = "B";

//     else if (currentStudentGrade >= 80)
//         currentStudentLetterGrade = "B-";

//     else if (currentStudentGrade >= 77)
//         currentStudentLetterGrade = "C+";

//     else if (currentStudentGrade >= 73)
//         currentStudentLetterGrade = "C";

//     else if (currentStudentGrade >= 70)
//         currentStudentLetterGrade = "C-";

//     else if (currentStudentGrade >= 67)
//         currentStudentLetterGrade = "D+";

//     else if (currentStudentGrade >= 63)
//         currentStudentLetterGrade = "D";

//     else if (currentStudentGrade >= 60)
//         currentStudentLetterGrade = "D-";

//     else
//         currentStudentLetterGrade = "F";

//     Console.WriteLine($"{currentStudent}\t\t{currentStudentGrade}\t{currentStudentLetterGrade}");
// }

// Console.WriteLine("Press the Enter key to continue");
// Console.ReadLine();




// int examAssignments = 5;

// string[] studentNames = new string[] { "Sophia", "Andrew", "Emma", "Logan" };

// int[] sophiaScores = new int[] { 90, 86, 87, 98, 100, 94, 90 };
// int[] andrewScores = new int[] { 92, 89, 81, 96, 90, 89 };
// int[] emmaScores = new int[] { 90, 85, 87, 98, 68, 89, 89, 89 };
// int[] loganScores = new int[] { 90, 95, 87, 88, 96, 96 };

// int[] studentScores = new int[10];

// string currentStudentLetterGrade = "";

// // display the header row for scores/grades
// Console.Clear();
// Console.WriteLine("Student\t\tExam Score\tOverall Grade\tExtra Credit\n");

// /*
// The outer foreach loop is used to:
// - iterate through student names 
// - assign a student's grades to the studentScores array
// - sum assignment scores (inner foreach loop)
// - calculate numeric and letter grade
// - write the score report information
// */
// foreach (string name in studentNames)
// {
//     string currentStudent = name;

//     if (currentStudent == "Sophia")
//         studentScores = sophiaScores;

//     else if (currentStudent == "Andrew")
//         studentScores = andrewScores;

//     else if (currentStudent == "Emma")
//         studentScores = emmaScores;

//     else if (currentStudent == "Logan")
//         studentScores = loganScores;


//     int sumAssignmentScores = 0;

//     decimal examScore = 0;

//     decimal currentStudentGrade = 0;

//     int gradedAssignments = 0;

//     decimal extraCredit = 0;

//     decimal creditoExtra = 0;

//     int gradedAssignmentsExtra = 0;



//     /* 
//     the inner foreach loop sums assignment scores
//     extra credit assignments are worth 10% of an exam score
//     */
//     foreach (int score in studentScores)
//     {
//         gradedAssignments += 1;

//         if (gradedAssignments <= examAssignments)
//         {
//             sumAssignmentScores += score;
//         }

//         else
//         {
//             gradedAssignmentsExtra += 1;
//             extraCredit += score;
//         }
//     }
//     decimal puntuacionFinal = 0;

//     examScore = (decimal)sumAssignmentScores/examAssignments;
//     creditoExtra = extraCredit/10/examAssignments;
//     currentStudentGrade = examScore + creditoExtra;
//     puntuacionFinal = extraCredit/gradedAssignmentsExtra;



//     if (currentStudentGrade >= 97)
//         currentStudentLetterGrade = "A+";

//     else if (currentStudentGrade >= 93)
//         currentStudentLetterGrade = "A";

//     else if (currentStudentGrade >= 90)
//         currentStudentLetterGrade = "A-";

//     else if (currentStudentGrade >= 87)
//         currentStudentLetterGrade = "B+";

//     else if (currentStudentGrade >= 83)
//         currentStudentLetterGrade = "B";

//     else if (currentStudentGrade >= 80)
//         currentStudentLetterGrade = "B-";

//     else if (currentStudentGrade >= 77)
//         currentStudentLetterGrade = "C+";

//     else if (currentStudentGrade >= 73)
//         currentStudentLetterGrade = "C";

//     else if (currentStudentGrade >= 70)
//         currentStudentLetterGrade = "C-";

//     else if (currentStudentGrade >= 67)
//         currentStudentLetterGrade = "D+";

//     else if (currentStudentGrade >= 63)
//         currentStudentLetterGrade = "D";

//     else if (currentStudentGrade >= 60)
//         currentStudentLetterGrade = "D-";

//     else
//         currentStudentLetterGrade = "F";

//     // Student         Grade
//     // Sophia:         92.2    A-

//     Console.WriteLine($"{currentStudent}\t\t{examScore}\t\t{currentStudentGrade}\t{currentStudentLetterGrade}\t{puntuacionFinal} ({creditoExtra} pts)");
// }

// // required for running in VS Code (keeps the Output windows open to view results)
// //Console.WriteLine("\n\rPress the Enter key to continue");
// // Console.ReadLine();


// string message = "The quick brown fox jumps over the lazy dog.";
// Console.WriteLine(message.Contains("fox"));
// Console.WriteLine(message.Contains("cow"));

// // These two lines of code will create the same output

// Console.WriteLine(message.Contains("fox") == false);
// Console.WriteLine(!message.Contains("fox"));




// //OPERADOR LOGICO CONDICIONAL
// int saleAmount = 1001;
// // int discount = saleAmount > 1000 ? 100 : 50;
// Console.WriteLine($"Discount: {(saleAmount > 1000 ? 100 : 50)}");

// Random coin = new Random();

// int coinSide = coin.Next(1, 3);

// Console.WriteLine($"The coin fall in: {(coinSide == 1 ? "Heads" : "Tails")} ");


// ejemplo de codigo de if y operador logico
// string permission = "Admin|Manager";
// int level = 55;
// string message = "";

// if (permission.Contains("Admin"))
// {
//     message = level > 55 ? "Welcome, super admin user." : "Welcome, admi user.";
// }
// else if (permission.Contains("Director"))
// {
//     message = level > 20 ? "Contact an admin for access" : "You do not have sufficient privileges";
// }
// else
//     message = "You do not have sufficient privileges to access";

// Console.WriteLine(message);


// string name = "steve";
// if (name == "bob")
//     Console.WriteLine("Found Bob");
// else if (name == "steve")
//     Console.WriteLine("Found Steve");
// else
//     Console.WriteLine("Found Chuck");



// int employeeLevel = 200;
// string employeeName = "John Smith";

// string title = "";

// switch (employeeLevel)
// {
//     case 100:
//         title = "Junior Associate";
//         break;
//     case 200:
//         title = "Senior Associate";
//         break;
//     case 300:
//         title = "Manager";
//         break;
//     case 400:
//         title = "Senior Manager";
//         break;
//     default:
//         title = "Associate";
//         break;
// }

// // version mejorada
// // title = employeeLevel switch
// // {
// //     100 => "Junior Associate",
// //     200 => "Senior Associate",
// //     300 => "Manager",
// //     400 => "Senior Manager",
// //     _ => "Associate",
// // };

// Console.WriteLine($"{employeeName}, {title}");

/*
// SKU = Stock Keeping Unit. 
// SKU value format: <product #>-<2-letter color code>-<size code>
string sku = "01-MN-L";

string[] product = sku.Split('-');

string type = "";
string color = "";
string size = "";

if (product[0] == "01")
{
    type = "Sweat shirt";
} else if (product[0] == "02")
{
    type = "T-Shirt";
} else if (product[0] == "03")
{
    type = "Sweat pants";
}
else
{
    type = "Other";
}

if (product[1] == "BL")
{
    color = "Black";
} else if (product[1] == "MN")
{
    color = "Maroon";
} else
{
    color = "White";
}

if (product[2] == "S")
{
    size = "Small";
} else if (product[2] == "M")
{
    size = "Medium";
} else if (product[2] == "L")
{
    size = "Large";
} else
{
    size = "One Size Fits All";
}

Console.WriteLine($"Product: {size} {color} {type}");
*/

// string sku = "08-MN-L";

// string[] product = sku.Split('-');

// string type = "";
// string color = "";
// string size = "";

// switch (product[0])
// {
//     case "01":
//         type = "Sweat shirt";
//         break;
//     case "02":
//         type = "T-shirt";
//         break;
//     case "03":
//         type = "Sweat pants";
//         break;
//     default:
//         type = "Others";
//         break;
// }

// switch (product[1])
// {
//     case "BL":
//         color = "Black";
//         break;
//     case "MN":
//         color = "Maroon";
//         break;
//     default:
//         color = "White";
//         break;
// }

// switch (product[2])
// {
//     case "S":
//         size = "Small";
//         break;
//     case "M":
//         size = "Medium";
//         break;
//     case "L":
//         size = "Large";
//         break;
//     default:
//         size = "One Size Fits All";
//         break;
// }

// Console.WriteLine($"Product: {size} {color} {type}");

// for (int i = 1; i < 10; i++)
// {
//     Console.WriteLine(i);
//     if (i == 7) break;
// }

// string [] names = {"Alex", "Eddi", "David", "Michael"};
// for (int i = names.Length - 1; i >=0; i-- )
// {
//     Console.WriteLine(names[i]);
// }

// string[] names = { "Alex", "Eddie", "David", "Michael" };

// for (int i = 0; i < names.Length; i++)
//     if (names[i] == "David") names[i] = "Sammy";

// foreach (string name in names) Console.WriteLine(name);


// string clave = "";

// for (int counter = 1; counter <= 100; counter++)
// {
//     if (counter % 3 == 0 && counter % 5 == 0)
//         clave = "FizzBuzz";
//     else if (counter % 5 == 0)
//         clave = "Buzz";
//     else if (counter % 3 == 0)
//         clave = "Fizz";
//     else clave = "";

//     Console.WriteLine($"{counter} {clave}");
// }


// do while
// Random random = new Random();

// int current = 0;

// do
// {
//     current = random.Next(1, 11);
//     Console.WriteLine(current);

// } while (current != 7);


// // while
// Random random = new Random();
// int current = random.Next(1, 11);

// while (current >= 3)
// {
//     Console.WriteLine(current);
//     current = random.Next(1, 11);
// }

// Console.WriteLine($"Last number: {current}");


// Random random = new Random();

// int current = random.Next(1, 11);

// do
// {
//     current = random.Next(1, 11);

//     if (current >= 8) continue;
    
//     Console.WriteLine(current);
// } while (current != 7);

Random random = new Random();
int ataque = random.Next(1, 11);

int vidaHeroe = 10;
int vidaVillano = 10;


while (vidaHeroe > 0 || vidaVillano > 0)
{
    ataque = random.Next(1, 11);
    vidaVillano -= ataque;
    Console.WriteLine($"ataque {ataque}");
    Console.WriteLine($" vida villano {vidaVillano}");

    ataque = random.Next(1, 11);
    vidaHeroe -= ataque;
    Console.WriteLine($"ataque {ataque}");
    Console.WriteLine($" vida heroe {vidaHeroe}");
}

// do
// {
//     ataque = random.Next(1, 11);
//     vidaVillano -= ataque;
//     vidaHeroe -= ataque;
//     Console.WriteLine($"Monster was damaged and lost {ataque} health and now has {vidaVillano} health.");
//     Console.WriteLine($"Hero was damaged and lost {ataque} health and now has {vidaHeroe} health.");


// } while (vidaHeroe == 0 || vidaVillano == 0);

// do
// {
//     ataque = random.Next(1, 11);
//     vidaHeroe -= ataque;
//     Console.WriteLine($"Monster was damaged and lost {ataque} health and now has {vidaHeroe} health.");

// } while (vidaVillano == 0);

// while (vidaHeroe >= 0)
// {
//     vidaVillano -= ataque;
//     Console.WriteLine($"Monster was damaged and lost {ataque} health and now has {vidaVillano} health.");
// }

// while (vidaVillano >= 0)
// {
//     vidaHeroe -= ataque;
//     Console.WriteLine($"Hero was damaged and lost {ataque} health and now has {vidaHeroe} health.");
// }