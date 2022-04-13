$(document).on('submit','#post-form',function(e){
    e.preventDefault();
    var data = new FormData();
    data.append('username',$('#username').val());
    data.append('room_id',$('#room_id').val());
    data.append('message',$('#message').val());
    data.append('username',$('#username').val());
    data.append('mfile',document.getElementById("f").files[0]);
    data.append("csrfmiddlewaretoken",$('input[name=csrfmiddlewaretoken]').val());
    $.ajax({
      type:'POST',
      url:'/chat/send',
      data: data,
      contentType:false,
      processData:false,
      success: function(data){
        //alert(data)
      }
    });
    document.getElementById('f').value = '';
    document.getElementById('message').value = '';
  });
  function checkFileExist(urlToFile) {
    var xhr = new XMLHttpRequest();
    xhr.open('HEAD', urlToFile, false);
    xhr.send();
    
    if (xhr.status == "404") {
      return false;
    } else {
      //alarm("true");
      return true;
    }
  }
  function checkIfImageExists(url, callback) {
    const img = new Image();
    img.src = url;
    if (img.complete) {
      callback(true);
    } else {
      img.onload = () => {
        callback(true);
      };
      img.onerror = () => {
        callback(false);
      };
    }
  }
  function isFileImage(file) {
    const acceptedImageTypes = ['image/gif', 'image/jpeg', 'image/png'];
    return file && $.inArray(file['type'], acceptedImageTypes)
  }
  $(document).ready(function(){
  setInterval(function(){
      $.ajax({
          type: 'GET',
          url : "/chat/get_messages/{{room}}/",
          success: function(response){
              console.log(response);
              $("#display").empty();
              for (var key in response.messages.reverse()){
                var file = "../media/"+response.messages[key].file;
                //var file = new File("../media/"+img);
                var temp = "<div class='container darker'>";
                temp += "<b>"+response.messages[key].user+"</b>";
                temp += "<p>"+response.messages[key].value+"</p>";
                
                
                if(isFileImage(file)){
                  checkIfImageExists(file,(exist)=>{
                    if(exist){
                      temp += "<img class=\"img-thumbnail imgmsg\"  src="+file+">";
                    }
                  });
                } else {
                  temp += "<div style=display:flex; flex-direction: horizontal>";
                    temp += "<img src=../media/file.png class=img-thumbnail width=40 height=40>";
                    temp += "<b>"+file+"</b>";
                  temp += "</div>";
                }
                temp += "</div>";
                $("#display").append(temp);
              }
          },
          error: function(response){
              alert('An error occured')
          }
      });
  },1000);
  })