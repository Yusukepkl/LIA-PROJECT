import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 400
    title: "Lia"

    Rectangle {
        anchors.fill: parent
        color: "black"

        Text {
            anchors.centerIn: parent
            text: "Modelo 3D aqui"
            color: "white"
        }
    }
}
