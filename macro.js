import xapi from 'xapi';
let i=0
function alert(title, text, duration = 3) {
  delay(text,duration)
  
}
function delay(text,duration){
  
setTimeout(function() {
  console.log(text[i])
xapi.Command.UserInterface.Message.TextLine.Display(
    { Duration: duration, Text: text[i] });
    i++;
    if(i<text.length){
      delay(text,duration)
    }
}, 3000);
}

xapi.Event.UserInterface.Assistant.Notification.on((event) => {
  const { Name, Payload } =  event;
  const jsonPayload = JSON.parse(Payload);
  alert(Name, jsonPayload.text);
});

xapi.Event.UserInterface.WebView.on((event)=>{
  console.log("Web view event",JSON.stringify(event))
})
