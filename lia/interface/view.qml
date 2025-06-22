import QtQuick
import QtQuick.Window
import QtQuick3D

Window {
    id: root
    visible: true
    width: 800
    height: 600
    title: "Lia"

    MouseArea {
        anchors.fill: parent
        onPositionChanged: (mouse) => {
            liaModel.lookX = mouse.x / root.width - 0.5
            liaModel.lookY = mouse.y / root.height - 0.5
        }
    }

    View3D {
        anchors.fill: parent

        Node {
            id: scene

            Model {
                id: liaModel
                source: "Lia.glb" // modelo fictício
                property real lookX: 0
                property real lookY: 0
            }
        }
    }
}
