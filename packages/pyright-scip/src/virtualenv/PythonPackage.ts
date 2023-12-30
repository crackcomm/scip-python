import * as path from 'path';

const validExtensions = new Set(['.py', '.pyi']);

export default class PythonPackage {
    constructor(public name: string, public version: string, public files: string[]) {}

    static fromPipShow(output: string): PythonPackage {
        let name = '';
        let version = '';
        let files: string[] = [];

        let gettingFiles = false;
        for (let line of output.split('\n')) {
            if (!line.trim()) {
                continue;
            }

            let split = line.split(':', 2);
            if (split.length == 2) {
                switch (split[0]) {
                    case 'Name':
                        name = split[1].trim();
                        break;
                    case 'Version':
                        version = split[1].trim();
                    case 'Files':
                        gettingFiles = true;
                }
            } else {
                if (!gettingFiles) {
                    throw 'Unexpected. Thought I should be getting files now';
                }

                line = line.trim();

                // Skip cached or out of project rfiles
                if (line.startsWith('..') || line.includes('__pycache__')) {
                    continue;
                }

                // Only include extensions that we care about
                if (!validExtensions.has(path.extname(line))) {
                    continue;
                }

                files.push(line);
            }
        }

        return new PythonPackage(name, version, files);
    }
}
