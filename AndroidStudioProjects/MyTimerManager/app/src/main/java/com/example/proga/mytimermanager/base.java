package com.example.proga.mytimermanager;

import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.CalendarView;
import android.widget.ListView;

import java.util.Calendar;
import java.util.Locale;

public class base extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_base);
        CalendarView calendar = (CalendarView)findViewById(R.id.calendar);
        Calendar currentdate = Calendar.getInstance(Locale.getDefault());
        calendar.setFirstDayOfWeek(Calendar.MONDAY);
        calendar.setOnDateChangeListener(new CalendarView.OnDateChangeListener() {
            @Override
            public void onSelectedDayChange(@NonNull CalendarView calendarView, int i, int i1, int i2) {
                Intent about_day = new Intent (base.this,about.class);
                startActivity(about_day);
            }
        });

    }
}
