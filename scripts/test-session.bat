@echo off
setlocal enabledelayedexpansion

REM Fixed identifiers for testing
set APP_NAME=terminal
set USER_ID=test-user-123
set SESSION_ID=test-session-456
set BASE_URL=http://localhost:8000

echo Creating session...
echo App: %APP_NAME%
echo User: %USER_ID%
echo Session: %SESSION_ID%
echo.

REM Create session
curl -X POST "%BASE_URL%/apps/%APP_NAME%/users/%USER_ID%/sessions/%SESSION_ID%" ^
  -H "Content-Type: application/json" ^
  -d "{}"

echo.
echo.
echo ============================================
echo First request to run_sse endpoint
echo ============================================
echo.

REM First request to run_sse
curl -X POST "%BASE_URL%/run_sse" ^
  -H "Content-Type: application/json" ^
  -d "{\"appName\": \"%APP_NAME%\", \"userId\": \"%USER_ID%\", \"sessionId\": \"%SESSION_ID%\", \"newMessage\": {\"role\": \"user\", \"parts\": [{\"text\": \"I'm using FastAPI to build a web application\"}]}, \"streaming\": false}"

echo.
echo.
echo ============================================
echo Second request to run_sse endpoint
echo ============================================
echo.

REM Second request to run_sse
curl -X POST "%BASE_URL%/run_sse" ^
  -H "Content-Type: application/json" ^
  -d "{\"appName\": \"%APP_NAME%\", \"userId\": \"%USER_ID%\", \"sessionId\": \"%SESSION_ID%\", \"newMessage\": {\"role\": \"user\", \"parts\": [{\"text\": \"Which framework did I use to build the web application?\"}]}, \"streaming\": false}"

echo.
echo.
echo Done!
pause
