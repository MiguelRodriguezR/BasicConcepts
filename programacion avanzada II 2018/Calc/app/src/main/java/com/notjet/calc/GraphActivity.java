package com.notjet.calc;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

public class GraphActivity extends AppCompatActivity {

    GraphView graph;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_graph);
        graph = (GraphView) findViewById(R.id.graph);
        drawGraph();
    }

    private DataPoint[] generateData() {
        int count = 9;
        DataPoint[] values = new DataPoint[count];
        int x=-4;
        for (int i=0; i<count; i++) {

            DataPoint v = new DataPoint(x, (x*x));
            x+=1;
            values[i] = v;
        }
        return values;
    }

    private void drawGraph() {
        graph.getViewport().setXAxisBoundsManual(true);
        graph.getViewport().setMinX(-10);
        graph.getViewport().setMaxX(10);

        graph.getViewport().setYAxisBoundsManual(true);
        graph.getViewport().setMinY(-10);
        graph.getViewport().setMaxY(10);

        graph.getViewport().setScalable(true);
        graph.getViewport().setScalableY(true);
        graph.getViewport().setScrollable(true);
        graph.getViewport().setScrollableY(true);



        LineGraphSeries<DataPoint> series = new LineGraphSeries<>(generateData());
        graph.addSeries(series);
    }


}
