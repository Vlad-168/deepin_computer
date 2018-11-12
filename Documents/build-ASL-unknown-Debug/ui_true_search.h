/********************************************************************************
** Form generated from reading UI file 'true_search.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TRUE_SEARCH_H
#define UI_TRUE_SEARCH_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QHeaderView>

QT_BEGIN_NAMESPACE

class Ui_True_Search
{
public:
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *True_Search)
    {
        if (True_Search->objectName().isEmpty())
            True_Search->setObjectName(QStringLiteral("True_Search"));
        True_Search->resize(400, 300);
        buttonBox = new QDialogButtonBox(True_Search);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setGeometry(QRect(30, 240, 341, 32));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        retranslateUi(True_Search);
        QObject::connect(buttonBox, SIGNAL(accepted()), True_Search, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), True_Search, SLOT(reject()));

        QMetaObject::connectSlotsByName(True_Search);
    } // setupUi

    void retranslateUi(QDialog *True_Search)
    {
        True_Search->setWindowTitle(QApplication::translate("True_Search", "Dialog", nullptr));
    } // retranslateUi

};

namespace Ui {
    class True_Search: public Ui_True_Search {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TRUE_SEARCH_H
