async function getMediaDevices() {
    return await navigator.mediaDevices.enumerateDevices();
}

async function getMusicOutputDevice() {
    return (await getMediaDevices()).find(a => a.label.toLowerCase().includes("youtube") && a.kind == "audiooutput");
}

async function getDefaultOutputDevice() {
    return (await getMediaDevices()).find(a => a.label.toLowerCase().includes("default") && a.kind == "audiooutput");
}

async function updateAllSinks(device) {
    document.querySelectorAll("video,audio").forEach(a => {
        if (a.sinkId != device.deviceId) {
            a.setSinkId(device.deviceId);
            console.log("[SOURCE] One Source has been updated with the required SinkID");
        }
    });
}

function changeVolume(v) {
    let audios = [...document.querySelectorAll("video, audio")];
    audios.forEach(a => a.volume = v);
}

function changeMuted(v) {
    let audios = [...document.querySelectorAll("video, audio")];
    audios.forEach(a => a.muted = v);
}

function resetAllSinks() {

}