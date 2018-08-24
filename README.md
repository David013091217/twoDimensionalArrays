# CLASSES AND FUNCTIONS
## There are two classes in order to save data in the customized 2D array:
* cell
  * each element in the array is one of these.
  * this is a built-in class, you won't use it really often
* tdArr
  * this class is where you build your customized array
  * this is how you build your array:
    > _\<array name\> tarray name = tdArr(\<array width\>, \<array hight\>, \<array to cover\>)_
  * there are several functions in the class:
    * _\_setup()_ 
      * after you build your array, you'll need to use this function to prepare your array
    > _\<array name\>.\_setup()_
    
    * _\_edit()_
      * this function helps to edit elements in array
    > _\<array name\>.\_edit(\<edit X\>, \<edit Y\>, \<edit value\>)_
    
    * _\_output()_
      * this function outputs the whole array
    > _\<array name\>.\_output()_
