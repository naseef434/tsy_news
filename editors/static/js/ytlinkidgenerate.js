/**
 * Created by RA on 11-Oct-20.
 */
function youtube_parser(){
    var idt = document.getElementById("y_link").value;
    function getId(link){
        return link.split('/').pop().split('?').pop().split('v=').pop();
    };
    var id = getId(idt);
    document.getElementById("y_id").value = id;

    }
