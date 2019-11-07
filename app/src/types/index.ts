export enum Priority {
  Undetermined = 'Undetermined',
  Critical = 'Critical',
  High = 'High',
  Medium = 'Medium',
  Low = 'Low',
}

export interface Client {
  id: number;
  name: string;
}

export default interface FeatureRequest {
  id?: number;
  title: string;
  description: string;
  client?: Client;
  priority: Priority;
  target_date: string;
  created_at?: string;
}
