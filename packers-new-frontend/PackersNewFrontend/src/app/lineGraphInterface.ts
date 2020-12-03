export interface DataPoint {
    name: Date;
    value: number;
}

export interface LineGraphData {
    name: string;
    series: DataPoint[];
}