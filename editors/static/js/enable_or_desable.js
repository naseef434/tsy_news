function toggle_district(selectedRadioId, targetId){
 if(selectedRadioId == "Kerala"){
  document.getElementById(targetId).style.display = "inline";
  document.getElementById("id_district").disabled = false;
 }
 else if(selectedRadioId != "kerala"){
  document.getElementById(targetId).style.display = "none";
  document.getElementById("id_district").disabled = true;
 }
}

function toggle_place(){
				if(document.getElementById("id_district").value == "11"){
					document.getElementById("id_place_div").style.display = "inline";
					document.getElementById("id_place").disabled = false;
				}
				else{
					document.getElementById("id_place_div").style.display = "none";
					document.getElementById("id_place").disabled = true;
				}
			}

function toggle_y_link_y(){
				if(document.getElementById("y_Yes").value == "Yes"){
					document.getElementById("image_field").style.display = "none";
					document.getElementById("image_field").disabled = true;
					document.getElementById("y_link_div").style.display = "inline";
					document.getElementById("y_link_div").disabled = false;
				}
				else{
					document.getElementById("image_field").style.display = "inline";
					document.getElementById("image_field").disabled = false;
					document.getElementById("y_link_div").style.display = "none";
					document.getElementById("y_link_div").disabled = true;
				}
			}


function toggle_y_link_n(){
				if(document.getElementById("y_No").value == "No"){
					document.getElementById("image_field").style.display = "block";
					document.getElementById("image_field").disabled = false;
					document.getElementById("y_link_div").style.display = "none";
					document.getElementById("y_link_div").disabled = true;
				}
				else{
					document.getElementById("image_field").style.display = "none";
					document.getElementById("image_field").disabled = true;
					document.getElementById("y_link_div").style.display = "inline";
					document.getElementById("y_link_div").disabled = false;
				}
			}