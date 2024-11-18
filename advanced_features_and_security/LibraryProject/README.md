# Django Permissions and Groups Setup

## Overview
This Django application implements a system of permissions and groups to control access to the book management system.

## Custom Permissions
- **can_view**: Allows viewing of books.
- **can_create**: Allows creating new books.
- **can_edit**: Allows editing existing books.
- **can_delete**: Allows deleting books.

## Groups
- **Editors**: Can create and edit books.
- **Viewers**: Can view books only.
- **Admins**: Can manage all aspects of books (view, create, edit, delete).

## Implementation
Permissions are enforced in views using the `@permission_required` decorator. Users must be assigned to appropriate groups to access functionalities according to their permissions.

## Testing
Users should be tested by logging in with different roles to ensure proper permission enforcement.
