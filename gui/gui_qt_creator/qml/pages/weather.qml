import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.0
import QtQuick.Timeline 1.0
import QtGraphicalEffects 1.15
import "../components"


Window {
    id: window
    width: 680
    height: 790
    visible: true
    color: "#00000000"
    title: qsTr("Weather")
    flags: Qt.FramelessWindowHint | Qt.Window
    Component.onCompleted: {
        backend.setStaticInfo()
        window.visible = true
    }

    Rectangle{
        id: bg
        width: 600
        color: "#9913151a"
        radius: 10
        anchors.fill: parent
        clip: true
        anchors.margins: 10
        z: 1

        CustomButton {
            id: btnClose
            x: 20
            width: 30
            height: 30
            opacity: 1
            text: "X"
            anchors.right: parent.right
            anchors.top: parent.top
            colorDefault: "#a4ebf3"
            anchors.topMargin: 15
            font.pointSize: 10
            font.family: "Segoe UI"
            anchors.rightMargin: 20
            colorMouseOver: "#a1cae2"
            colorPressed: "#28527a"
            onClicked: window.close()
        }

        Rectangle {
            id: rectangleTitle
            height: 30
            opacity: 1
            color: "#a4ebf3"
            radius: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.leftMargin: 20
            anchors.rightMargin: 60
            anchors.topMargin: 15

            Row {
                width: 72
                height: 23
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.verticalCenterOffset: 1
                Text {
                    color: "#3f4801"
                    text: qsTr("Weather ")
                    horizontalAlignment: Text.AlignLeft
                    font.pointSize: 10
                    font.family: "Segoe UI"
                }
                anchors.leftMargin: 279
            }

            DragHandler {
                onActiveChanged: if (active) { window.startSystemMove() }
                target: null
            }
        }

        Row {
            id: row
            height: 200
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            leftPadding: 20
            spacing: 10
            anchors.leftMargin: 0
            anchors.topMargin: 60
            anchors.rightMargin: 0

            CircularProgressBar {
                id: percentage_CPU
                width: 200
                height: 200
                opacity: 0
                text: "°C"
                value: 0
                startAngle: 90
                Text {
                    color: "#a4ebf3"
                    text: qsTr("Temperature")
                    anchors.bottom: parent.bottom
                    font.family: "Segoe UI"
                    font.pointSize: 16
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottomMargin: 40
                }
                progressColor: "#a4ebf3"
                progressWidth: 6
                textSize: 14
                roundCap: false
                strokeBgWidth: 6
                bgStrokeColor: "#101010"
            }

            CircularProgressBar {
                id: percentage_RAM
                width: 200
                height: 200
                opacity: 0
                text: "Km/h"
                value: 0
                startAngle: 90
                Text {
                    color: "#a4ebf3"
                    text: qsTr("Wind")
                    anchors.bottom: parent.bottom
                    font.family: "Segoe UI"
                    font.pointSize: 16
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottomMargin: 40
                }
                progressColor: "#a4ebf3"
                progressWidth: 6
                strokeBgWidth: 6
                roundCap: false
                textSize: 14
                bgStrokeColor: "#101010"
            }

            CircularProgressBar {
                id: percentage_GPU
                width: 200
                height: 200
                opacity: 1
                value: 0
                startAngle: 90
                Text {
                    color: "#a4ebf3"
                    text: qsTr("Humidity")
                    anchors.bottom: parent.bottom
                    font.family: "Segoe UI"
                    font.pointSize: 16
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottomMargin: 40
                }
                progressColor: "#a4ebf3"
                progressWidth: 6
                strokeBgWidth: 6
                roundCap: false
                textSize: 14
                bgStrokeColor: "#101010"
            }
        }

        Rectangle {
            id: infos
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: row.bottom
            anchors.rightMargin: 20
            anchors.leftMargin: 20
            anchors.topMargin: 15
            Layout.maximumWidth: 380
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            Layout.preferredHeight: 390
            Layout.preferredWidth: 280

            Column{
                id: column
                anchors.fill: parent
                spacing: 10

                Rectangle{
                    id: info_cpu_title
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#a4ebf3"
                    radius: 5

                    Rectangle{
                        height: 35
                        color: "#08090b"
                        radius: 5
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.rightMargin: 5
                        anchors.leftMargin: 5

                        Row {
                            x: 69
                            anchors.fill: parent
                            anchors.rightMargin: 263
                            anchors.bottomMargin: 0
                            anchors.leftMargin: 263
                            anchors.topMargin: 0
                            padding: 10

                            Text {
                                visible: true
                                color: "#a4ebf3"
                                text: qsTr("Weather")
                                anchors.verticalCenter: parent.verticalCenter
                                font.pointSize: 10
                                font.family: "Segoe UI"
                            }
                        }
                    }
                }

                Rectangle{
                    id: rectangle1
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#0c0d10"
                    radius: 5

                    Row {
                        anchors.fill: parent
                        padding: 10

                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Weather Description:")
                            anchors.verticalCenter: parent.verticalCenter
                        }
                        Text {
                            id: cpu_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            font.pointSize: 8
                            leftPadding: 5
                        }
                    }
                }

                Rectangle{
                    id: rectangle2
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#0c0d10"
                    radius: 5

                    Row {
                        anchors.fill: parent
                        padding: 10

                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Humidity :")
                            anchors.verticalCenter: parent.verticalCenter
                        }
                        Text {
                            id: cpu_frequency_physical_cores_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            font.pointSize: 8
                            leftPadding: 5
                        }

                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Pressure:")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 10
                        }

                        Text {
                            id: cpu_frequency_total_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 5
                            font.pointSize: 8
                        }
                    }
                }

                Rectangle{
                    id: rectangle3
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#0c0d10"
                    radius: 5

                    Row {
                        anchors.fill: parent
                        padding: 10

                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Temperature| Max:")
                            anchors.verticalCenter: parent.verticalCenter
                        }
                        Text {
                            id: cpu_frequency_max_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            font.pointSize: 8
                            leftPadding: 5
                        }

                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Min:")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 10
                        }

                        Text {
                            id: cpu_frequency_min_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 5
                            font.pointSize: 8
                        }
                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Current:")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 10
                        }

                        Text {
                            id: cpu_frequency_current_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 5
                            font.pointSize: 8
                        }
                    }
                }

                Rectangle{
                    id: info_ram_title
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#a4ebf3"
                    radius: 5

                    Rectangle{
                        height: 35
                        color: "#08090b"
                        radius: 5
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.rightMargin: 5
                        anchors.leftMargin: 5

                        Row {
                            anchors.fill: parent
                            anchors.bottomMargin: 0
                            anchors.leftMargin: 273
                            anchors.topMargin: 0
                            anchors.rightMargin: 273
                            padding: 10

                            Text {
                                color: "#a4ebf3"
                                text: qsTr("Wind")
                                anchors.verticalCenter: parent.verticalCenter
                                font.pointSize: 10
                                font.family: "Segoe UI"
                            }
                        }
                    }
                }

                Rectangle {
                    id: rectangle4
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#0c0d10"
                    radius: 5
                    Row {
                        anchors.fill: parent
                        padding: 10

                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Speed:")
                            anchors.verticalCenter: parent.verticalCenter
                        }
                        Text {
                            id: ram_total_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            font.pointSize: 8
                            leftPadding: 5
                        }

                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Degree:")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 10
                        }

                        Text {
                            id: ram_available_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 5
                            font.pointSize: 8
                        }
                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Clouds:")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 10
                        }

                        Text {
                            id: ram_used_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 5
                            font.pointSize: 8
                        }
                    }
                }

                Rectangle{
                    id: info_gpu_title
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#a4ebf3"
                    radius: 5

                    Rectangle{
                        height: 35
                        color: "#08090b"
                        radius: 5
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.rightMargin: 5
                        anchors.leftMargin: 5

                        Row {
                            anchors.fill: parent
                            anchors.bottomMargin: 0
                            anchors.leftMargin: 253
                            anchors.topMargin: 0
                            anchors.rightMargin: 253
                            padding: 10

                            Text {
                                color: "#a4ebf3"
                                text: qsTr("Description")
                                anchors.verticalCenter: parent.verticalCenter
                                font.pointSize: 10
                                font.family: "Segoe UI"
                            }
                        }
                    }
                }

                Rectangle {
                    id: rectangle5
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#0c0d10"
                    radius: 5
                    Row {
                        anchors.fill: parent
                        padding: 10
                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Description:")
                            anchors.verticalCenter: parent.verticalCenter
                        }

                        Text {
                            id: gpu_model_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 5
                            font.pointSize: 8
                        }
                    }
                }

                Rectangle {
                    id: rectangle6
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#0c0d10"
                    radius: 5
                    Row {
                        anchors.fill: parent
                        padding: 10
                        Text {
                            color: "#a4ebf3"
                            text: qsTr("City:")
                            anchors.verticalCenter: parent.verticalCenter
                        }

                        Text {
                            id: vram_total_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 5
                            font.pointSize: 8
                        }

                    }
                }

                Rectangle {
                    id: rectangle7
                    width: parent.width
                    height: 35
                    opacity: 1
                    color: "#0c0d10"
                    radius: 5
                    Row {
                        anchors.fill: parent
                        padding: 10
                        Text {
                            color: "#a4ebf3"
                            text: qsTr("Country:")
                            anchors.verticalCenter: parent.verticalCenter
                        }

                        Text {
                            id: gpu_temp_info
                            color: "#878787"
                            text: qsTr("---")
                            anchors.verticalCenter: parent.verticalCenter
                            leftPadding: 5
                            font.pointSize: 8
                        }
                    }
                }
            }
        }

        Rectangle{
            id: rectangle
            height: 30
            opacity: 1
            color: "#a4ebf3"
            radius: 10
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.rightMargin: 20
            anchors.leftMargin: 20
            anchors.bottomMargin: 15

            Row {
                id: column3
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 10


            }
        }
    }

    DropShadow{
        anchors.fill: bg
        source: bg
        verticalOffset: 0
        horizontalOffset: 0
        radius: 10
        samples: 12
        color: "#b3000000"
        z: 0
    }

    Connections{
        target: backend

        // STATIC INFO
        function onCpuInfo(argument) { cpu_info.text = argument }
        function onCpuPhysicalCoresInfo(argument) { cpu_frequency_physical_cores_info.text = argument }
        function onCpuTotalCoresInfo(argument) { cpu_frequency_total_info.text = argument }
        function onCpuFrequencyMaxInfo(argument) { cpu_frequency_max_info.text = argument }
        function onCpuFrequencyMinInfo(argument) { cpu_frequency_min_info.text = argument }
        function onRamTotalInfo(argument) { ram_total_info.text = argument }
        function onGpuModelInfo(argument) { gpu_model_info.text = argument }
        function onVramTotalInfo(argument) { vram_total_info.text = argument }

        // DYNAMIC INFO
        function onPercentageCPU(argument) { percentage_CPU.value = argument }
        function onPercentageRAM(argument) { percentage_RAM.value = argument }
        function onPercentageGPU(argument) { percentage_GPU.value = argument }
        function onCpuFrequencyCurrentInfo(argument) { cpu_frequency_current_info.text = argument }
        function onRamAvailableInfo(argument) { ram_available_info.text = argument }
        function onRamUsedInfo(argument) { ram_used_info.text = argument }
        function onGpuTempInfo(argument) { gpu_temp_info.text = argument }
    }

    Text {
        id: text1
        x: 25
        color: "#878787"
        text: qsTr("Version: 1.0.0")
        anchors.right: parent.right
        anchors.top: parent.top
        font.pixelSize: 12
        horizontalAlignment: Text.AlignRight
        verticalAlignment: Text.AlignVCenter
        anchors.topMargin: 32
        anchors.rightMargin: 80
        font.family: "Segoe UI"
    }



    Timeline {
        id: timeline
        animations: [
            TimelineAnimation {
                id: timelineAnimation
                running: true
                loops: 1
                duration: 3000
                to: 3000
                from: 0
            }
        ]
        endFrame: 3000
        enabled: true
        startFrame: 0

        KeyframeGroup {
            target: percentage_CPU
            property: "opacity"
            Keyframe {
                frame: 800
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: percentage_RAM
            property: "opacity"
            Keyframe {
                frame: 1000
                value: 1
            }

            Keyframe {
                frame: 200
                value: 0
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: percentage_CPU
            property: "value"
            Keyframe {
                easing.bezierCurve: [0.664,0.0036,0.334,1,1,1]
                frame: 1100
                value: 100
            }

            Keyframe {
                frame: 0
                value: 0
            }

            Keyframe {
                frame: 1600
                value: 0
            }
        }

        KeyframeGroup {
            target: percentage_RAM
            property: "value"
            Keyframe {
                frame: 200
                value: 0
            }

            Keyframe {
                frame: 0
                value: 0
            }

            Keyframe {
                easing.bezierCurve: [0.664,0.0036,0.334,1,1,1]
                frame: 1298
                value: 100
            }

            Keyframe {
                frame: 1800
                value: 0
            }
        }

        KeyframeGroup {
            target: percentage_GPU
            property: "value"
            Keyframe {
                frame: 400
                value: 0
            }

            Keyframe {
                frame: 0
                value: 0
            }

            Keyframe {
                easing.bezierCurve: [0.664,0.0036,0.334,1,1,1]
                frame: 1500
                value: 100
            }

            Keyframe {
                frame: 2000
                value: 0
            }
        }

        KeyframeGroup {
            target: percentage_GPU
            property: "opacity"
            Keyframe {
                frame: 399
                value: 0
            }

            Keyframe {
                frame: 1200
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: info_cpu_title
            property: "opacity"
            Keyframe {
                frame: 1201
                value: 0
            }

            Keyframe {
                frame: 1600
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: rectangle1
            property: "opacity"
            Keyframe {
                frame: 1298
                value: 0
            }

            Keyframe {
                frame: 1700
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: rectangle2
            property: "opacity"
            Keyframe {
                frame: 1399
                value: 0
            }

            Keyframe {
                frame: 1800
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: rectangle3
            property: "opacity"
            Keyframe {
                frame: 1500
                value: 0
            }

            Keyframe {
                frame: 1900
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: info_ram_title
            property: "opacity"
            Keyframe {
                frame: 1601
                value: 0
            }

            Keyframe {
                frame: 2000
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: rectangle4
            property: "opacity"
            Keyframe {
                frame: 1699
                value: 0
            }

            Keyframe {
                frame: 2100
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: info_gpu_title
            property: "opacity"
            Keyframe {
                frame: 1800
                value: 0
            }

            Keyframe {
                frame: 2200
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: rectangle5
            property: "opacity"
            Keyframe {
                frame: 1901
                value: 0
            }

            Keyframe {
                frame: 2300
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: rectangle6
            property: "opacity"
            Keyframe {
                frame: 2002
                value: 0
            }

            Keyframe {
                frame: 2400
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: rectangle7
            property: "opacity"
            Keyframe {
                frame: 2099
                value: 0
            }

            Keyframe {
                frame: 2500
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: rectangle
            property: "opacity"
            Keyframe {
                frame: 2200
                value: 0
            }

            Keyframe {
                frame: 2600
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }
    }
}

