/********************************************************************************
** Form generated from reading UI file 'vvod_id.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_VVOD_ID_H
#define UI_VVOD_ID_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Vvod_ID
{
public:
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QLineEdit *name;
    QLineEdit *fename;
    QLineEdit *third_name;
    QLabel *label_2;
    QPushButton *search_button;

    void setupUi(QDialog *Vvod_ID)
    {
        if (Vvod_ID->objectName().isEmpty())
            Vvod_ID->setObjectName(QStringLiteral("Vvod_ID"));
        Vvod_ID->resize(414, 240);
        verticalLayout = new QVBoxLayout(Vvod_ID);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        label = new QLabel(Vvod_ID);
        label->setObjectName(QStringLiteral("label"));

        verticalLayout->addWidget(label);

        name = new QLineEdit(Vvod_ID);
        name->setObjectName(QStringLiteral("name"));

        verticalLayout->addWidget(name);

        fename = new QLineEdit(Vvod_ID);
        fename->setObjectName(QStringLiteral("fename"));

        verticalLayout->addWidget(fename);

        third_name = new QLineEdit(Vvod_ID);
        third_name->setObjectName(QStringLiteral("third_name"));

        verticalLayout->addWidget(third_name);

        label_2 = new QLabel(Vvod_ID);
        label_2->setObjectName(QStringLiteral("label_2"));

        verticalLayout->addWidget(label_2);

        search_button = new QPushButton(Vvod_ID);
        search_button->setObjectName(QStringLiteral("search_button"));

        verticalLayout->addWidget(search_button);


        retranslateUi(Vvod_ID);

        QMetaObject::connectSlotsByName(Vvod_ID);
    } // setupUi

    void retranslateUi(QDialog *Vvod_ID)
    {
        Vvod_ID->setWindowTitle(QApplication::translate("Vvod_ID", "\320\222\320\262\320\276\320\264 \320\264\320\260\320\275\320\275\321\213\321\205", nullptr));
        label->setText(QString());
        label_2->setText(QString());
        search_button->setText(QApplication::translate("Vvod_ID", "ok", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Vvod_ID: public Ui_Vvod_ID {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_VVOD_ID_H
