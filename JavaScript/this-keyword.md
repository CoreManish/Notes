### I observed few things and want to share with all of you.
In one line, `this` keyword-
- Inside Regular function : represents the object under which function is sitting or object who calls the function.
- Inside Arrow function : `this` inside an arrow function is equivalent to the global object.

## Detailed explanation
### Regular function
```
const obj = {
            val1: 30,
            val2: 40,
            add: function () {
                return this.val1 + this.val2; 
            }
        }
```
        let x = obj.add();
        console.log(x);

In the above example, function `add` is sitting inside an object `obj` , so keyword `this` used inside function will represent `obj`.
##### Lets look an another example
```
function test() {
            console.log(this.innerHeight);
        }
```
```
 test();
```
Here function `test` is sitting inside `window` (Global) object. So `this` keyword used inside `test` function will represent `window` object.
We know `window` object has certain properties associated with them like *innerHeight*, *innerWidth* [etc](https://www.geeksforgeeks.org/properties-of-window-object/).

### Arrow function
```
 const address={
            name:"Peter",
            age: 26,
            something: () => {
               return this.innerHeight;
            }
        }
```
        console.log(address.something());

Although function `something` is sitting inside an object `address` but `this` keyword used inside function will represent the global object. And so, like 2nd example we can access the properties of global object here.

##### Please mention any mistake
Manish
