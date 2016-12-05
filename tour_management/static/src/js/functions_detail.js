function passenger_detail(val,ad)
{
     if(ad==1)
        {
            var element = $("input.no_of_adults");
            var i;
            for(i=1;i<=val;i++)
            {
              var adult_name = 'adult_name' + i
              var adult_age = 'adult_age' + i
              var adult_gender = 'adult_gender' + i
              element.parent().append("<br/>Name:<input type='text' name=" + adult_name + " value=''/>Age:<input type='text' name="+ adult_age+" value=''/><input type='radio' name="+ adult_gender+" value='Male'/>Male<input type='radio' name="+ adult_gender+" value='Female'/>Female");
              console.log("Element >>>>>>>>>>.",element.parent());
            }
               console.log('js called for no of adult');
         }
    else if(ad==2)
         {
            var element = $("input.no_of_childs");
            var i;
            for(i=1;i<=val;i++)
              {
                 var child_name = 'child_name' + i
                 var child_age = 'child_age' + i
                 var child_gender = 'child_gender' + i
                 element.parent().append("<br/>Name:<input type='text' name="+ child_name+" value=''/>Age:<input type='text' name="+ child_age +" value=''/><input type='radio' name="+ child_gender +" value='Male'/>Male<input type='radio' name="+ child_gender +" value='Female'/>Female");
                 console.log("Element >>>>>>>>>>.",element.parent());
              }

                 console.log('js call for no of child');
          }
    else if(ad==3)
         {
            var element = $("input.no_of_infants");
            var i;
            for(i=1;i<=val;i++)
            {
               var infant_name = 'infant_name' + i
               var infant_age = 'infant_age' + i
               var infant_gender = 'infant_gender' + i
               element.parent().append("<br/>Name:<input type='text' name="+ infant_name +" value=''/>Age:<input type='text' name="+ infant_age +" value=''/><input type='radio' name="+ infant_gender +" value='Male'/>Male<input type='radio' name="+ infant_gender +" value='FeMale'/>Female");
               console.log("Element >>>>>>>>>>.",element.parent());
            }
            console.log('js call for no of infant');
          }
}