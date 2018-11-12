/********************************************************************************
** Form generated from reading UI file 'give_book.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_GIVE_BOOK_H
#define UI_GIVE_BOOK_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_give_book
{
public:
    QMenuBar *menubar;
    QWidget *centralwidget;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *give_book)
    {
        if (give_book->objectName().isEmpty())
            give_book->setObjectName(QStringLiteral("give_book"));
        give_book->resize(800, 600);
        menubar = new QMenuBar(give_book);
        menubar->setObjectName(QStringLiteral("menubar"));
        give_book->setMenuBar(menubar);
        centralwidget = new QWidget(give_book);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        give_book->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(give_book);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        give_book->setStatusBar(statusbar);

        retranslateUi(give_book);

        QMetaObject::connectSlotsByName(give_book);
    } // setupUi

    void retranslateUi(QMainWindow *give_book)
    {
        give_book->setWindowTitle(QApplication::translate("give_book", "MainWindow", nullptr));
    } // retranslateUi

};

namespace Ui {
    class give_book: public Ui_give_book {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GIVE_BOOK_H
