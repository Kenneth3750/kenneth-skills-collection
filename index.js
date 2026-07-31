#!/usr/bin/env node

const { execSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
const command = args[0];
const filter = args[1] || '';

const scripts = {
  'install:claude': 'scripts/install-claude.sh',
  'install:opencode': 'scripts/install-opencode.sh',
  'install:all': 'scripts/sync-skills.sh',
};

if (!command || !scripts[command]) {
  console.log('Kenneth Skills Collection');
  console.log('');
  console.log('Usage:');
  console.log('  npx kenneth-skills-collection install:claude [category|category/skill]');
  console.log('  npx kenneth-skills-collection install:opencode [category|category/skill]');
  console.log('  npx kenneth-skills-collection install:all [category|category/skill]');
  console.log('');
  console.log('Examples:');
  console.log('  npx kenneth-skills-collection install:claude              # All skills for Claude');
  console.log('  npx kenneth-skills-collection install:claude aws          # All AWS skills');
  console.log('  npx kenneth-skills-collection install:claude aws/aws-costs # Specific skill');
  console.log('');
  process.exit(command ? 1 : 0);
}

const scriptPath = path.join(__dirname, scripts[command]);

try {
  const cmd = filter ? `bash "${scriptPath}" "${filter}"` : `bash "${scriptPath}"`;
  execSync(cmd, { stdio: 'inherit' });
} catch (error) {
  console.error(`Error running ${command}:`, error.message);
  process.exit(1);
}
