import QtQuick
import QtQuick.Window
import QtQuick3D
import QtQuick.Controls

Window {
    id: root
    visible: true
    width: 800
    height: 600
    title: "Lia"
    property var controller: modelController

    MouseArea {
        anchors.fill: parent
        hoverEnabled: true
        onPositionChanged: (mouse) => {
            if (root.controller) {
                root.controller.look_at(mouse.x / root.width,
                                        mouse.y / root.height)
            }
        }
    }

    View3D {
        anchors.fill: parent

        Node {
            id: scene

            Model {
                id: liaModel
                source: Qt.resolvedUrl("../../assets/Lia.glb")
            }
        }
    }

    Component.onCompleted: {
        if (root.controller) {
            root.controller.set_model(liaModel)
        }
    }
}
