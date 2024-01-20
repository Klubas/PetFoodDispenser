const rootAddress = window.location.href

console.log(rootAddress)

const callEndpoint = async (method, endpoint, data = null) => {
     const url = rootAddress + endpoint
     const settings = {
        method: method,
        headers: {
              'Accept': 'application/json',
              'Content-Type': 'text/html'
        }
     }

     if (data){
        settings.headers['Content-Type'] = 'application/json'
        settings.body = JSON.stringify(data)
     }

     let response

     await fetch(url, settings)
        .then(response => response.json())
        .then(jsonData => response = jsonData.message)

     try {
        switch (response.status) {
              case 'SUCCESS':
                 console.log("OK")
                 return response
              case 'ERROR':
                 console.log("ERROR")
                 throw new Error('Unexpected error: ' + response.description)
              default:
                 console.log(response)
                 console.log("DEFAULT")
                 throw new Error(response.response)
        }
     } catch (error) {
        console.log(error)
        console.log("CATCH")
        throw new Error(error)
     }
}

const open = (open_angle) => {
     buttonOpen.disabled = true
     return callEndpoint('POST'
     , '/api/dispenser/open?open_angle=' + open_angle)
           .then(response => buttonOpen.disabled = false)
}

const close = (close_angle) => {
     buttonClose.disabled = true
     return callEndpoint('POST'
     , '/api/dispenser/close?close_angle=' + close_angle)
           .then(response => buttonClose.disabled = false)
}

const feed = (open_angle, close_angle, open_seconds) => {
     buttonFeed.disabled = true
     return callEndpoint('POST'
     , '/api/dispenser/feed?open_angle=' + open_angle + '&close_angle=' + close_angle + '&open_seconds=' + open_seconds)
           .then(response => response.picture ? pictureImg.src = "data:image/jpeg;base64," + response.picture : null)
           .then(response => buttonFeed.disabled = false)
}

const takePhoto = () => {
     buttonPhoto.disabled = true
     return callEndpoint('GET'
     , '/api/camera/capture')
           .then(response => response.picture ? pictureImg.src = "data:image/jpeg;base64," + response.picture : null)
           .then(response => buttonPhoto.disabled = false)
}

const getCamera = () => {
     buttonPhoto.disabled = true
     return callEndpoint('GET'
     , '/api/camera')
           .then(response => response.device ? buttonPhoto.disabled = false : buttonPhoto.disabled = true)
}

const openAngleInput   = document.getElementById('open-angle-input')
const closeAngleInput  = document.getElementById('close-angle-input')
const openSecondsInput = document.getElementById('open-seconds-input')
const buttonFeed       = document.getElementById('feed-button')
const buttonOpen       = document.getElementById('open-button')
const buttonClose      = document.getElementById('close-button')
const buttonPhoto      = document.getElementById('photo-button')
const pictureImg       = document.getElementById('picture-img')

buttonOpen.addEventListener('click',
    function(){open(openAngleInput.value)}
)

buttonClose.addEventListener('click',
    function(){close(closeAngleInput.value)}
)

buttonFeed.addEventListener('click',
    function(){feed(openAngleInput.value, closeAngleInput.value, openSecondsInput.value)}
)

buttonPhoto.addEventListener('click',
    function(){takePhoto()}
)

getCamera()
