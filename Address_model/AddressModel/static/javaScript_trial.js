<script type="text/javascript">
function FillAddressInput()
    {
       let checkBox= document.getElementById('checkBox');
       let flat_no = document.getElementById("id_flat_no");
       let street_name = document.getElementById("id_street_name")
       let city = document.getElementById("id_city")
       let pincode = document.getElementById("id_pincode")
       let area = document.getElementById("id_area")
       let landmark = document.getElementById("id_landmark")
       let district = document.getElementById("id_district")
       let state = document.getElementById("id_state")
       let country = document.getElementById("id_country")


       let Cflat_no = document.getElementById("id_Cflat_no");
       let Cstreet_name = document.getElementById("id_Cstreet_name");
       let Ccity = document.getElementById("id_Ccity");
       let Cpincode = document.getElementById("id_Cpincode");
       let Carea = document.getElementById("id_Carea");
       let Clandmark = document.getElementById("id_Clandmark");
       let Cdistrict = document.getElementById("id_Cdistrict");
       let Cstate = document.getElementById("id_Cstate");
       let Ccountry = document.getElementById("id_Ccountry");


        if (checkBox.checked == true)
        {

       let flat_noValue = flat_no.value;
       let street_nameValue = street_name.value;
       let cityValue = city.value;
       let pincodeValue = pincode.value;
       let areaValue = area.value;
       let landmarkValue = landmark.value;
       let districtValue = district.value;
       let stateValue = state.value;
       let countryValue = country.value;

       Cflat_no.value = flat_no.value;
       Cstreet_name.value = street_name.value;
       Ccity.value = city.value;
       Cpincode.value = pincode.value;
       Carea.value = area.value;
       Clandmark.value = landmark.value;
       Cdistrict.value = district.value;
       Cstate.value = state.value;
       Ccountry.value = country.value;

       }
        else
        {

       Cflat_no.value = "";
       Cstreet_name.value ="";
       Ccity.value ="";
       Cpincode.value ="";
       Carea.value ="";
       Clandmark.value ="";
       Cdistrict.value ="";
       Cstate.value ="";
       Ccountry.value = "";

                 }
    }
</script>