print("hello")
num=5;
print("the number is ",num);
floatnum= 5.8;
print("the floating point number is",floatnum);
name="piya";
print("the int number is:",num," and the floating point number is:",floatnum," and the name is:",name);
def convert_to_fahren(celcius):
    fahrenheit=(celcius*(9/5))+32;
    return fahrenheit;

print(type(num));
#taking the user input
celcius=input("Enter the temperture in celcius:")
print(convert_to_fahren(float(celcius)));
#celcius=32.5;
#to convert celcius to fahrenheit
#fahrenheit=(celcius*(9/5))+32;
#print("the temperture in fahrenheit is:",fahrenheit);

