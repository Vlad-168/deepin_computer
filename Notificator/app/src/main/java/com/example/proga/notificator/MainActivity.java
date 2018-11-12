package com.example.proga.notificator;

import android.app.AlarmManager;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.res.Resources;
import android.graphics.BitmapFactory;
import android.provider.Settings;
import android.support.v4.app.NotificationCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.Calendar;

public class MainActivity extends AppCompatActivity{
    private static final int NOTIFY_ID = 101;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btn = (Button)findViewById(R.id.btn);
        TextView request = (TextView)findViewById(R.id.text);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                RequestQu
            }
        });
        GlobalVars.value +=1;
        if (GlobalVars.value > 0) {
            Intent notificationIntent = new Intent(MainActivity.this, MainActivity.class);
            PendingIntent contentIntent = PendingIntent.getActivity(MainActivity.this,
                    0, notificationIntent,
                    PendingIntent.FLAG_CANCEL_CURRENT);
            AlarmManager alarm = (AlarmManager) getApplicationContext().getSystemService(Context.ALARM_SERVICE);
            Calendar calendar = Calendar.getInstance();
            calendar.set(Calendar.HOUR_OF_DAY,21);
            calendar.set(Calendar.MINUTE,39);
            calendar.set(Calendar.SECOND,00);
            alarm.setRepeating(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(),
                    1000*60*60*24,contentIntent);
            Resources res = MainActivity.this.getResources();
            NotificationCompat.Builder builder = new NotificationCompat.Builder(MainActivity.this);

            builder.setContentIntent(contentIntent)
                    // îáÿçàòåëüíûå íàñòðîéêè
                    .setSmallIcon(R.drawable.foodfreelogo)
                    //.setContentTitle(res.getString(R.string.notifytitle)) // Çàãîëîâîê óâåäîìëåíèÿ
                    .setContentTitle("Внимание!!!")
                    //.setContentText(res.getString(R.string.notifytext))
                    .setContentText("Время выпить таблетку") // Òåêñò óâåäîìëåíèÿ
                    // íåîáÿçàòåëüíûå íàñòðîéêè
                    .setLargeIcon(BitmapFactory.decodeResource(res, R.drawable.foodfreelogo)) // áîëüøàÿ
                    // êàðòèíêà
                    //.setTicker(res.getString(R.string.warning)) // òåêñò â ñòðîêå ñîñòîÿíèÿ
                    .setTicker("Успейте до конца")
                    .setWhen(System.currentTimeMillis())
                    .setAutoCancel(true); // àâòîìàòè÷åñêè çàêðûòü óâåäîìëåíèå ïîñëå íàæàòèÿ

            NotificationManager notificationManager =
                    (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
            // Àëüòåðíàòèâíûé âàðèàíò
            // NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this);

            notificationManager.notify(NOTIFY_ID, builder.build());
            

        } else {
        }

    }
}


