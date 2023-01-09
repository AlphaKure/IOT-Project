

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function addHours(numOfHours, date = new Date()) {
    date.setTime(date.getTime() + numOfHours * 60 * 60 * 1000);
  
    return date;
}

var userID=getCookie('userID');

$.ajax({
        url:'https://iot-scatter8.azurewebsites.net/api/GETalluserdata',
        type:"POST",
        data:JSON.stringify({'UserID':userID}),
        contentType:"application/json; charset=utf-8",
        dataType:"JSON",
        success:function(result){
            var i=0;
            if (result.length==0){
                $("#table").hide();
                $("#label").text("我沒有你的資料QQ");
                return
            }
            while(result[i]!=undefined){
                row=result[i];
                if (row['userid']!=null){
                    let realTime=new Date(row['datetime']);
                    realTime=addHours(8,realTime);
                    $("#table >tbody").append('<tr><td>'+$.format.date(realTime, 'yyyy/MM/dd HH:mm:ss')+'</td><td>'+row['weight']+'</td></tr>')
                }
                i+=1;
            }
}})

