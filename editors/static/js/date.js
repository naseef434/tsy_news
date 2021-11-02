var d = new Date();
        var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        document.getElementById("month").innerHTML = months[d.getMonth()];
        document.getElementById("date").innerHTML = d.getDate();
        document.getElementById("year").innerHTML = d.getFullYear();


va