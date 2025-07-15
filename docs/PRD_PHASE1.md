## Tax Advisor Application - Phase 1 Development Plan

### Overview
A web-based platform for salaried individuals to analyze tax liabilities and receive personalized, AI-powered tax-saving strategies. **Phase 1** focuses on project setup, database schema creation, and the landing page.

### Phase 1 Scope
| Phase   | Deliverable/Feature         | Acceptance Criteria                                                                 |
|---------|----------------------------|-------------------------------------------------------------------------------------|
| Phase 1 | Project setup, DB schema, landing page | User sees the landing page, and the `UserFinancials` table exists in Supabase. |

### Core Requirements
- Set up the project repository and initial file structure.
- Implement the Supabase database schema with the `UserFinancials` table.
- Create a modern, branded landing page as the application's entry point.

### Tech Stack (Phase 1)
| Component | Technology |
|-----------|------------|
| Frontend  | Vanilla HTML, CSS (Aptos Display font), JavaScript |
| Backend   | Python (FastAPI) |
| Database  | Supabase (Cloud PostgreSQL, direct psycopg2 connection) |

### Database Schema: `UserFinancials`
| Column Name         | Data Type         | Description                        |
|--------------------|------------------|------------------------------------|
| `session_id`       | `UUID`           | Primary Key, unique session identifier |
| `gross_salary`     | `NUMERIC(15, 2)` | Total gross salary                 |
| `basic_salary`     | `NUMERIC(15, 2)` | Basic salary component             |
| `hra_received`     | `NUMERIC(15, 2)` | HRA received                       |
| `rent_paid`        | `NUMERIC(15, 2)` | Annual rent paid                   |
| `deduction_80c`    | `NUMERIC(15, 2)` | 80C investments                    |
| `deduction_80d`    | `NUMERIC(15, 2)` | 80D medical insurance              |
| `standard_deduction`| `NUMERIC(15, 2)`| Standard deduction                 |
| `professional_tax` | `NUMERIC(15, 2)` | Professional tax paid              |
| `tds`              | `NUMERIC(15, 2)` | Tax Deducted at Source             |
| `created_at`       | `TIMESTAMPTZ`    | Record creation timestamp          |

### UI/UX Principles (Landing Page)
- Modern, light theme with blue highlights.
- Typography: Use the "Aptos Display" font for a distinct look.
- Responsive and visually appealing design.

### Acceptance Criteria
- The project repository is initialized and structured.
- The `UserFinancials` table is created in Supabase with the specified schema.
- The landing page is accessible and matches the design principles outlined above. 