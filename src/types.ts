export interface AccountResponse {
  user: {
    id: string;
    github: string;
    displayName: string;
    is_active: boolean;
    created: Date;
    updated: Date;
  };
  access: string;
  refresh: string;
}
