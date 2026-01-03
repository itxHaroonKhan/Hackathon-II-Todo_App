# Research Findings: Phase II — Full-Stack Web Todo Application

## Neon PostgreSQL Connection String Format

**Decision**: Use standard PostgreSQL connection string format for Neon
**Rationale**: Neon is PostgreSQL-compatible, so the standard format works with additional query parameters for connection pooling
**Format**: `postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require`
**Alternative considered**: Different proprietary formats (rejected as unnecessary)

## Next.js Project Setup Specifics

**Decision**: Use standard Next.js 14 with App Router
**Rationale**: Latest stable version with modern React patterns and server-side rendering capabilities
**Structure**:
- Pages in `app/` directory
- API routes in `app/api/`
- Components in `components/`
- Services/utils in `lib/` or `services/`
**Alternative considered**: Pages Router (older approach, less suitable for new projects)

## CORS Configuration Requirements

**Decision**: Configure CORS middleware in FastAPI to allow specific origins
**Rationale**: Essential for security and proper communication between frontend and backend
**Implementation**: Use `CORSMiddleware` with allowed origins, methods, and headers
**Configuration**:
- Allow origins: ['http://localhost:3000'] for development
- Allow methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
- Allow headers: ['Content-Type', 'Accept']
**Alternative considered**: Allow all origins (rejected for security reasons)

## Additional Technical Decisions

### Database Connection Pooling
**Decision**: Use SQLModel's async engine with proper connection pooling
**Rationale**: Neon handles connection pooling, but proper async engine configuration is needed
**Implementation**: Configure `asyncio`-compatible connection pool settings

### Environment Configuration
**Decision**: Use python-dotenv for environment variable management
**Rationale**: Standard approach in Python projects, integrates well with FastAPI
**Implementation**: Load .env file at application startup, validate required variables

### Error Handling Strategy
**Decision**: Implement custom exception handlers in FastAPI
**Rationale**: Provides consistent error responses across all endpoints
**Implementation**: Use FastAPI's exception handling with custom HTTPException subclasses